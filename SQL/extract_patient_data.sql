SELECT
  case when p.sex = 1 then '003'
       when p.sex = 2 then '004'
   end as 'คำนำหน้า',
  p.fname AS "ชื่อ",
  p.lname AS "นามสกุล",
  p.sex AS "เพศ",
  RIGHT(CONCAT('0', DAY(p.birthdate)), 2) AS "วันเกิด",
  RIGHT(CONCAT('0', MONTH(p.birthdate)), 2) AS "เดือนเกิด",
  YEAR(p.birthdate) AS "ปีเกิด",
  p.cid AS "เลขบัตรประชาชน",
  p.house_regist_type_id AS "ประเภทที่อยู่อาศัย",
  CONCAT(v.address_id, RIGHT(CONCAT('0', v.village_moo), 2)) AS "เลขที่อยู่อาศัย",
  v.village_name AS "ชื่อหมู่บ้าน",
  REGEXP_REPLACE(h.address, '[^0-9]', '') AS "บ้านเลขที่",
  h.road AS "ชื่อถนน"

FROM person p
LEFT JOIN pname p2 ON p.pname = p2.`name`
LEFT JOIN house h ON p.house_id = h.house_id
LEFT JOIN village v ON h.village_id = v.village_id
LEFT JOIN patient p3 ON p.patient_hn = p3.hn
WHERE p.house_regist_type_id IN (1, 3) 
  AND v.village_moo <> 0 
  AND p.nationality = 99 
  AND p.person_discharge_id = 9;
  and p.birthdate is not null
