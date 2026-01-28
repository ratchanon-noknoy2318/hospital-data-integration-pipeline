import pymysql
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv()

# 1. ตั้งค่าการเชื่อมต่อฐานข้อมูล
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'admin'),
    'password': os.getenv('DB_PASSWORD', '123456'),
    'database': os.getenv('DB_NAME', 'hosxp'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'charset': 'utf8'
}

def export_full_report():
    conn = None
    try:
        # 2. เชื่อมต่อ MySQL
        print("Connecting to the database...")
        conn = pymysql.connect(**db_config)
        print("Connection successful!")
        
        # 3. SQL Query (ชุดที่คุณให้มา)
        sql_query = """
        SELECT
            person.prename AS `คํานําหน้า`,
            person.fname AS `ชื่อ`,
            person.lname AS `นามสกุล`,
            person.sex AS `เพศ`,
            right(birth,2) AS `วันเกิด`,
            mid(birth,6,2) AS `เดือนเกิด`,
            YEAR(birth) AS `ปีเกิด`,
            person.idcard AS `เลขบัตรประชาชน`,
            person.typelive AS `ประเภทที่อยู่อาศัย`,
            house.villcode AS `เลขที่อยู่อาศัย`,
            village.villname AS `ชื่อหมู่บ้าน`,
            person.hnomoi AS `บ้านเลขที่`,
            house.road AS `ชื่อถนน`,
            house.xgis AS `ละติจูด`,
            house.ygis AS `ลองติจูด`
        FROM
            person
        INNER JOIN house ON person.hcode = house.hcode
        INNER JOIN village ON house.pcucode = village.pcucode AND house.villcode = village.villcode
        WHERE
            person.typelive IN(1,3) AND
            person.dischargetype = '9'
        """
        
        # 4. ดึงข้อมูลเข้า Pandas DataFrame
        print("Fetching data from database...")
        df = pd.read_sql(sql_query, conn)
        print(f"Fetched {len(df)} records.")

        if df.empty:
            print("No data found. The report will be empty.")
            return
        
        # --- [ 5. ส่วนจัดการข้อมูล (Data Transformation) ] ---
        
        # ก. รวมชื่อ-นามสกุล และลบช่องว่าง
        df['ชื่อ-นามสกุล'] = df['ชื่อ'].str.strip() + " " + df['นามสกุล'].str.strip()
        
        # ข. แปลงเพศ 1, 2 เป็น ชาย, หญิง
        df['เพศ'] = df['เพศ'].replace({1: 'ชาย', 2: 'หญิง', '1': 'ชาย', '2': 'หญิง'})
        
        # ค. คำนวณอายุ (ปีปัจจุบัน - ปีเกิด)
        this_year_buddhist = datetime.now().year + 543  # ใช้ปี พ.ศ.
        df['ปีเกิด'] = pd.to_numeric(df['ปีเกิด'], errors='coerce')
        df['อายุ'] = this_year_buddhist - df['ปีเกิด'].fillna(this_year_buddhist).astype(int)
        
        # ง. จัดการค่าว่าง (Null) ให้ดูสวยงาม
        df.fillna({'ชื่อถนน': '-', 'ละติจูด': 0, 'ลองติจูด': 0}, inplace=True)

        # จ. เลือกและเรียงลำดับคอลัมน์ที่จะเอาลง Excel
        final_columns = [
            'คํานําหน้า', 'ชื่อ-นามสกุล', 'เพศ', 'อายุ', 
            'เลขบัตรประชาชน', 'ชื่อหมู่บ้าน', 'บ้านเลขที่', 
            'ชื่อถนน', 'ละติจูด', 'ลองติจูด'
        ]
        df_final = df[final_columns]

        # --- [ 6. ส่งออกเป็นไฟล์ Excel ] ---
        filename = "Buddy_Care_Report.xlsx"
        
        # ใช้ Engine 'openpyxl' (ต้องติดตั้งด้วย: pip install openpyxl)
        df_final.to_excel(filename, index=False, sheet_name='Data_Patient')
        
        print("-" * 30)
        print(f"Success! File has been saved as: {filename}")
        print("-" * 30)

    except pymysql.Error as db_err:
        print(f"Database Error: {db_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if conn and conn.open:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    export_full_report()