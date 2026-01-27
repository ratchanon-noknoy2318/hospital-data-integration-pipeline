CREATE TABLE patients (
    user_id VARCHAR(100) PRIMARY KEY,
    citizen_id VARCHAR(13) UNIQUE,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    birth_year INT,
    age INT,
    gender INT COMMENT '1=ชาย, 2=หญิง',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;