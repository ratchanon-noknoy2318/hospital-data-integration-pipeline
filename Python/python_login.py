# 1. กำหนดข้อมูลที่ถูกต้องไว้ก่อน (ในอนาคตส่วนนี้จะมาจาก Database)
correct_username = "user123"
correct_password = "password789"

# 2. รับค่าจากผู้ใช้
print("--- ระบบเข้าสู่ระบบ ---")
user_input = input("Username: ")
pass_input = input("Password: ")

# 3. ตรวจสอบเงื่อนไข
if user_input == correct_username and pass_input == correct_password:
    print("ยินดีด้วย! คุณเข้าสู่ระบบสำเร็จ")
else:
    print("ขออภัย Username หรือ Password ไม่ถูกต้อง")