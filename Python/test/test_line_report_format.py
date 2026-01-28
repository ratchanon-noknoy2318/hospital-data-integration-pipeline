from datetime import datetime
from linebot import LineBotApi
from linebot.models import TextSendMessage

# 1. ใส่ Token ของคุณเพื่อทดสอบการส่งจริง
LINE_ACCESS_TOKEN = 'LINE_ACCESS_TOKEN'
USER_ID = 'USER_ID'

def test_report_format():
    # 2. จำลองข้อมูล (Mock Data) เหมือนที่ดึงมาจาก SQL
    # ใช้ List of Dictionaries แทน DataFrame (เหมือนที่ได้จาก pymysql DictCursor)
    rows = [
        {'clinic_name': 'อายุรกรรม', 'total': 120},
        {'clinic_name': 'ศัลยกรรม', 'total': 45},
        {'clinic_name': 'กุมารเวชกรรม', 'total': 30},
        {'clinic_name': 'ทันตกรรม', 'total': 15}
    ]
    
    yesterday = datetime.now().strftime('%Y-%m-%d')

    # 3. ส่วนของฟังก์ชันที่คุณต้องการทดสอบ
    if rows:
        report_msg = f"📊 [TEST] รายงานสรุปผู้ป่วยวันที่ {yesterday}\n"
        report_msg += "--------------------------\n"
        total_all = 0
        for row in rows:
            report_msg += f"🔹 {row['clinic_name']}: {row['total']} คน\n"
            total_all += row['total']
            
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
