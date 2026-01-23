CREATE TABLE patients (
    -- 1. ใช้ ID จาก Webhook เป็น Primary Key (เช่น U12345 หรือ UUID จากระบบอื่น)
    user_id VARCHAR(100) PRIMARY KEY,
    
    -- 2. ข้อมูลยืนยันตัวตน
    citizen_id VARCHAR(13) UNIQUE COMMENT 'เลขบัตรประชาชน 13 หลัก',
    
    -- 3. ข้อมูลชื่อ-นามสกุล
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    
    -- 4. ข้อมูลส่วนตัวและกายภาพ
    age TINYINT,
    gender TINYINT COMMENT '1 = ผู้ชาย, 2 = ผู้หญิง',
    
    -- 5. ข้อมูลที่อยู่
    district VARCHAR(100) COMMENT 'เขต หรือ อำเภอ',
    
    -- 6. ข้อมูลระบบและแหล่งที่มา
    provider VARCHAR(50) NOT NULL COMMENT 'เช่น line, hospital_portal, stripe',
    raw_payload JSON COMMENT 'เก็บ JSON ทั้งหมดที่ส่งมาจาก Webhook',
    
    -- 7. บันทึกเวลา
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;