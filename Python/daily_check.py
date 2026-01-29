import pymysql
from datetime import datetime, timedelta
from linebot import LineBotApi
from linebot.models import TextSendMessage
import os
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv()

LINE_ACCESS_TOKEN = os.getenv('LINE_ACCESS_TOKEN')
USER_ID = os.getenv('LINE_USER_ID')

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'charset': 'utf8'
}

def check_and_notify_line():
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    conn = None

    try:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()

        sql = """
        SELECT spclty.name AS clinic_name, COUNT(ovst.hn) AS total
        FROM ovst
        LEFT JOIN spclty ON spclty.spclty = ovst.spclty
        WHERE ovst.vstdate = %s
        GROUP BY spclty.name
        ORDER BY total DESC
        """
        cursor.execute(sql, (yesterday,))
        rows = cursor.fetchall()

        # สร้างข้อความรายงาน
        if rows:
            report_msg = f"📊 รายงานสรุปผู้ป่วยวันที่ {yesterday}\n"
            report_msg += "--------------------------\n"

            total_all = 0
            for clinic_name, total in rows:
                report_msg += f"🔹 {clinic_name}: {total} คน\n"
                total_all += total

            report_msg += "--------------------------\n"
            report_msg += f"✅ รวมทั้งสิ้น: {total_all} คน"
        else:
            report_msg = f"⚠️ วันที่ {yesterday} ไม่พบข้อมูลผู้ป่วยในระบบ"

        # ส่ง Line
        line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)
        line_bot_api.push_message(USER_ID, TextSendMessage(text=report_msg))
        print("✅ Line Notification Sent!")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    check_and_notify_line()
