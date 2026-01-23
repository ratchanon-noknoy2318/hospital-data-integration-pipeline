SELECT
    vl.village_moo,
    vl.village_name,
    ta.full_name
FROM village vl
LEFT JOIN thaiaddress ta ON ta.addressid = vl.address_id;