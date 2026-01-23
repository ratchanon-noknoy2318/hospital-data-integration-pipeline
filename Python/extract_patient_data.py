import pymysql
import pandas as pd

# 1. ตั้งค่าการเชื่อมต่อ (ปรับให้ตรงกับ Server ของคุณ)
db_config = {
    'host': 'localhost',
    'user': 'admin',
    'password': '123456',
    'database': 'hosxp', # เปลี่ยนเป็นชื่อ DB ของคุณ
    'port': 3306,
    'charset': 'utf8'
}

def export_patient_data():
    try:
        # 2. เชื่อมต่อ MySQL
        conn = pymysql.connect(**db_config)
        
        # 3. ใส่ SQL Query ที่คุณให้มา
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
            house.ygis AS `ลองติจูด`,
            '' AS `ประเภทผู้ป่วย`,
            '' AS หนังสือเดินทาง
        FROM
            person
        INNER JOIN house ON person.hcode = house.hcode
        INNER JOIN village ON house.pcucode = village.pcucode AND house.villcode = village.villcode
        WHERE
            person.typelive IN(1,3) AND
            person.dischargetype = '9'
        """
        
        # 4. ใช้ Pandas อ่านข้อมูลจาก SQL
        print("กำลังดึงข้อมูลจากระบบ Buddy-Care...")
        df = pd.read_sql(sql_query, conn)
        
        # 5. แสดงผล 5 แถวแรก
        print(df.head())
        
        # 6. (แถม) ส่งออกเป็นไฟล์ Excel
        # df.to_excel("patient_data.xlsx", index=False)
        # print("บันทึกไฟล์ patient_data.xlsx สำเร็จ!")

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    export_patient_data()