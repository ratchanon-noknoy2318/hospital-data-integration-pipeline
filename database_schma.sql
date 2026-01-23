CREATE TABLE patients (
    -- 1. Patient ID ที่รับมาจาก Webhook หรือระบบลงทะเบียนภายนอก
    patient_id VARCHAR(100) PRIMARY KEY,
    
    -- 2. ข้อมูลยืนยันตัวตนคนไข้
    citizen_id VARCHAR(13) UNIQUE COMMENT 'เลขบัตรประชาชน 13 หลัก',
    
    -- 3. ข้อมูลส่วนตัว
    first_name VARCHAR(100) COMMENT 'ชื่อจริงคนไข้',
    last_name VARCHAR(100) COMMENT 'นามสกุลคนไข้',
    age TINYINT COMMENT 'อายุ',
    gender TINYINT COMMENT '1 = ชาย, 2 = หญิง',
    
    -- 4. ข้อมูลที่อยู่
    district VARCHAR(100) COMMENT 'เขต/อำเภอ ที่คนไข้อยู่',
    
    -- 5. ข้อมูลระบบและ Webhook
    source_provider VARCHAR(50) NOT NULL COMMENT 'แหล่งที่มาของข้อมูลคนไข้',
    raw_payload JSON COMMENT 'ข้อมูลดิบทั้งหมดจาก Webhook',
    
    -- 6. บันทึกเวลา
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;