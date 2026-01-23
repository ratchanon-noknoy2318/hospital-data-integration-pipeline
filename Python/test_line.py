import pandas as pd
from datetime import datetime
from linebot import LineBotApi
from linebot.models import TextSendMessage
from dotenv import load_dotenv
import os

# โหลดค่าจากไฟล์ .env
load_dotenv()


# 1. ใส่ Token ของคุณเพื่อทดสอบการส่งจริง
LINE_ACCESS_TOKEN = os.getenv('LINE_ACCESS_TOKEN')
USER_ID = os.getenv('LINE_USER_ID')

def test_report_format():
    # 2. จำลองข้อมูล (Mock Data) เหมือนที่ดึงมาจาก SQL
    data = {
        'clinic_name': ['อายุรกรรม', 'ศัลยกรรม', 'กุมารเวชกรรม', 'ทันตกรรม'],
        'total': [120, 45, 30, 15]
    }
    df = pd.DataFrame(data)
    
    yesterday = datetime.now().strftime('%Y-%m-%d')

    # 3. ส่วนของฟังก์ชันที่คุณต้องการทดสอบ
    if not df.empty:
        report_msg = f"📊 [TEST] รายงานสรุปผู้ป่วยวันที่ {yesterday}\n"
        report_msg += "--------------------------\n"
        for index, row in df.iterrows():
            report_msg += f"🔹 {row['clinic_name']}: {row['total']} คน\n"
        
        total_all = df['total'].sum()
        report_msg += "--------------------------\n"
        report_msg += f"✅ รวมทั้งสิ้น: {total_all} คน"
    else:
        report_msg = f"⚠️ วันที่ {yesterday} ไม่พบข้อมูลผู้ป่วยในระบบ"

    # 4. พิมพ์ดูหน้าตาในจอดำก่อนส่ง
    print("--- Preview Message ---")
    print(report_msg)
    print("-----------------------")

    # 5. ลองส่งเข้า Line จริง
    try:
        line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)
        line_bot_api.push_message(USER_ID, TextSendMessage(text=report_msg))
        print("✅ Line Notification Sent Successfully!")
    except Exception as e:
        print(f"❌ Line Error: {e}")

if __name__ == "__main__":
    test_report_format()