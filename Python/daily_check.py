import pymysql
import pandas as pd
from datetime import datetime, timedelta
from linebot import LineBotApi
from linebot.models import TextSendMessage
import os
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv()

# --- ตั้งค่าส่วนตัว (ห้ามแชร์ให้คนอื่น) ---
LINE_ACCESS_TOKEN = os.getenv('LINE_ACCESS_TOKEN')
USER_ID = os.getenv('LINE_USER_ID')
db_config = {
    'host': os.getenv('DB_HOST'), 'user': os.getenv('DB_USER'), 'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'), 'port': int(os.getenv('DB_PORT', 3306)), 'charset': 'utf8'
}

def check_and_notify_line():
    # 1. เตรียมวันที่ (เมื่อวาน)
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    try:
        # 2. ดึงข้อมูลจาก MySQL
        conn = pymysql.connect(**db_config)
        sql = f"""
        SELECT spclty.name as clinic_name, COUNT(ovst.hn) as total
        FROM ovst
        LEFT JOIN spclty on spclty.spclty=ovst.spclty
        WHERE ovst.vstdate = '{yesterday}'
        GROUP BY spclty.name
        ORDER BY total DESC
        """
        
        # ใช้ Pandas ดึงข้อมูลและจัดการ DataFrame
        df = pd.read_sql(sql, conn)

        # 3. สร้างข้อความสำหรับรายงาน
        if not df.empty:
            report_msg = f"📊 รายงานสรุปผู้ป่วยวันที่ {yesterday}\n"
            report_msg += "--------------------------\n"
            
            for index, row in df.iterrows():
                report_msg += f"🔹 {row['clinic_name']}: {row['total']} คน\n"
            
            total_all = df['total'].sum()
            report_msg += "--------------------------\n"
            report_msg += f"✅ รวมทั้งสิ้น: {total_all} คน"
        else:
            report_msg = f"⚠️ วันที่ {yesterday} ไม่พบข้อมูลผู้ป่วยในระบบ"

        # 4. ส่งเข้า Line OA
        line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)
        line_bot_api.push_message(USER_ID, TextSendMessage(text=report_msg))
        print("✅ Line Notification Sent!")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    check_and_notify_line()