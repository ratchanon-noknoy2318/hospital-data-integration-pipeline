import pandas as pd

# 1. อ่านไฟล์ CSV เข้ามาเป็น DataFrame (ตาราง)
# ใช้ encoding='utf-8-sig' เพื่อรองรับภาษาไทยจาก Excel
df = pd.read_csv('patients_data.csv', encoding='utf-8-sig')

# 2. ล้างชื่อคอลัมน์ให้อัตโนมัติ (ตัดช่องว่างหน้า-หลัง)
df.columns = df.columns.str.strip()

print("--- ข้อมูลคนไข้ทั้งหมดจากตาราง ---")
print(df)

# 3. คัดกรองกลุ่มเสี่ยง (ความดันบน >= 140)
# นี่คือพลังของ Pandas: เขียนเงื่อนไขบรรทัดเดียวเหมือนใช้ Filter ใน Excel
high_risk = df[df['sys_bp'] >= 140]

print("\n--- ⚠️ รายชื่อกลุ่มเสี่ยงความดันสูง ---")
if high_risk.empty:
    print("ไม่พบคนไข้กลุ่มเสี่ยง")
else:
    print(high_risk[['id', 'name', 'sys_bp']])

# 4. ส่งออกผลลัพธ์เป็นไฟล์ใหม่ (Load)
high_risk.to_csv('urgent_patients.csv', index=False, encoding='utf-8-sig')
print("\n[สำเร็จ] ระบบบันทึกรายชื่อคนไข้ด่วนลงไฟล์ 'urgent_patients.csv' แล้ว")