import pymysql
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env เพื่อความปลอดภัย
# Make sure you have a .env file in the same directory with your DB credentials
# Example .env file:
# DB_HOST=localhost
# DB_USER=admin
# DB_PASSWORD=123456
# DB_NAME=hosxp
# DB_PORT=3306
load_dotenv()

# 1. ตั้งค่าการเชื่อมต่อฐานข้อมูลจาก Environment Variables
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'hosxp'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'charset': 'utf8'
}

def export_data_for_ai_audit():
    """
    ดึงข้อมูลผู้ป่วยในรูปแบบที่ลดทอนข้อมูลส่วนบุคคล (Pseudonymized)
    เพื่อส่งให้ AI ตรวจสอบความผิดปกติของข้อมูล โดยคำนึงถึง PDPA
    - ใช้ hn เป็นตัวระบุแทนชื่อและเลขบัตรประชาชน
    - ส่งออกเฉพาะข้อมูลที่จำเป็นต่อการวิเคราะห์ เช่น อายุ, เพศ, ที่อยู่ (ระดับหมู่บ้าน)
    """
    conn = None
    try:
        # 2. เชื่อมต่อ MySQL
        print("Connecting to the database for AI data export...")
        conn = pymysql.connect(**db_config)
        print("Connection successful.")

        # 3. SQL Query ที่เลือกเฉพาะข้อมูลที่จำเป็นและลดทอน PII
        # เราจะใช้ hn เป็น Primary Key สำหรับอ้างอิงกลับ แต่ไม่เปิดเผยชื่อหรือเลขบัตร
        sql_query = """
        SELECT
            p.hn,                           -- Pseudonym (ตัวระบุแทน)
            p.sex,                          -- เพศ
            p.birth,                        -- วันเดือนปีเกิด (สำหรับคำนวณอายุ)
            p.typelive,                     -- ประเภทที่อยู่อาศัย
            v.villname AS village_name,     -- ชื่อหมู่บ้าน
            h.xgis AS latitude,             -- ละติจูด
            h.ygis AS longitude             -- ลองติจูด
        FROM
            person p
        INNER JOIN house h ON p.hcode = h.hcode
        INNER JOIN village v ON h.pcucode = v.pcucode AND h.villcode = v.villcode
        WHERE
            p.typelive IN (1, 3) AND
            p.dischargetype = '9'
        """

        # 4. ดึงข้อมูลเข้า Pandas DataFrame
        print("Executing query and fetching data...")
        df = pd.read_sql(sql_query, conn)
        print(f"Fetched {len(df)} records for AI audit.")

        if df.empty:
            print("No data found matching the criteria. Exiting.")
            return

        # --- [ 5. ส่วนจัดการข้อมูล (Data Transformation) ] ---

        # ก. แปลงเพศ 1, 2 เป็น ชาย, หญิง
        df['gender'] = df['sex'].replace({1: 'Male', 2: 'Female', '1': 'Male', '2': 'Female'})

        # ข. คำนวณอายุ (ปีปัจจุบัน - ปีเกิด)
        birth_dates = pd.to_datetime(df['birth'], errors='coerce')
        current_year = datetime.now().year
        df['age'] = current_year - birth_dates.dt.year

        # ค. จัดการค่าว่าง (Null)
        df['latitude'] = df['latitude'].fillna(0.0)
        df['longitude'] = df['longitude'].fillna(0.0)
        df['age'] = df['age'].fillna(0).astype(int)

        # ง. เลือกและเปลี่ยนชื่อคอลัมน์สำหรับส่งออก
        final_columns = {
            'hn': 'patient_id', 'age': 'age', 'gender': 'gender',
            'typelive': 'residence_type', 'village_name': 'village_name',
            'latitude': 'latitude', 'longitude': 'longitude'
        }
        df_final = df[final_columns.keys()].rename(columns=final_columns)

        # --- [ 6. ส่งออกเป็นไฟล์ CSV (เหมาะกับงาน Data Science/AI) ] ---
        filename = "ai_audit_patient_data.csv"
        df_final.to_csv(filename, index=False, encoding='utf-8-sig')

        print("-" * 30, f"Successfully exported data for AI audit.\nFile saved as: {filename}", f"Columns exported: {list(df_final.columns)}", "-" * 30, sep="\n")

    except pymysql.Error as db_err:
        print(f"Database Error: {db_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    export_data_for_ai_audit()
