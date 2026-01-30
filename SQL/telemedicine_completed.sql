SELECT
    o.hn,
    CONCAT(p.pname, p.fname, ' ', p.lname) AS full_name,
    o.vstdate,
    vn.age_y,
    pt.name AS pttype_name,
    ic.tname AS pdx_name,
    vn.income
FROM ovst o
JOIN opitemrece oi
    ON o.vn = oi.vn
JOIN nondrugitems nd
    ON oi.icode = nd.icode
LEFT JOIN patient p
    ON o.hn = p.hn
LEFT JOIN vn_stat vn
    ON vn.vn = o.vn
LEFT JOIN pttype pt
    ON pt.pttype = vn.pttype
LEFT JOIN icd101 ic
    ON vn.pdx = ic.code
WHERE oi.icode = '3003921'
  AND o.vstdate BETWEEN '2025-01-01' AND '2025-06-16'
ORDER BY o.vstdate;
