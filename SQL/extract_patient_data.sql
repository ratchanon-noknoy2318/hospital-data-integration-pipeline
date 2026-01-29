SELECT
    CASE 
        WHEN p.sex = 1 THEN '003'
        WHEN p.sex = 2 THEN '004'
    END AS "คำนำหน้า",

    p.fname AS "ชื่อ",
    p.lname AS "นามสกุล",
    p.sex AS "เพศ",

    LPAD(DAY(p.birthdate), 2, '0')   AS "วันเกิด",
    LPAD(MONTH(p.birthdate), 2, '0') AS "เดือนเกิด",
    YEAR(p.birthdate)                AS "ปีเกิด",

    p.cid AS "เลขบัตรประชาชน",
    p.house_regist_type_id AS "ประเภทที่อยู่อาศัย",

    CONCAT(v.address_id, LPAD(v.village_moo, 2, '0')) AS "เลขที่อยู่อาศัย",
    v.village_name AS "ชื่อหมู่บ้าน",

    REGEXP_REPLACE(h.address, '[^0-9]', '') AS "บ้านเลขที่",
    h.road AS "ชื่อถนน"

FROM person p

INNER JOIN house h
        ON p.house_id = h.house_id

INNER JOIN village v
        ON h.village_id = v.village_id
       AND v.village_moo <> 0 

WHERE p.house_regist_type_id IN (1, 3)
  AND p.nationality = 99
  AND p.person_discharge_id = 9
  AND p.birthdate IS NOT NULL;
