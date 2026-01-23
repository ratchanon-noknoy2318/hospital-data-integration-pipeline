SELECT
person.prename AS `คํานําหน้า`,
person.fname AS `ชื่อ`,
person.lname AS `นามสกุล`,
person.sex AS `เพศ`,
right(birth,2) AS `วันเกิด`,
mid(birth,6,2) AS `เดือนเกิด`,
YEAR(birth) AS `ปีเกิด`,
person.idcard AS `เลขบัตรประชาชน`,
person.typelive AS `ประเภทที่อยู่อาศัย`,
house.villcode AS `เลขที่อยู่อาศัย`,
village.villname AS `ชื่อหมู่บ้าน`,
person.hnomoi AS `บ้านเลขที่`,
house.road AS `ชื่อถนน`,
house.xgis AS `ละติจูด`,
house.ygis AS `ลองติจูด`,
'' AS `ประเภทผู้ป่วย`,
'' AS หนังสือเดินทาง
FROM
person
INNER JOIN house ON person.hcode = house.hcode
INNER JOIN village ON house.pcucode = village.pcucode AND house.villcode = village.villcode
WHERE
person.typelive IN(1,3) AND
person.dischargetype = '9'