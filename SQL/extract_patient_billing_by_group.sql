SELECT
    o.hn,
    CONCAT(p.pname, p.fname, ' ', p.lname) AS full_name,
    o.vstdate,
    o.vsttime,
    nd.icode,
    nd.name AS service_name
FROM ovst o
JOIN opitemrece oi 
    ON o.vn = oi.vn
JOIN nondrugitems nd 
    ON oi.icode = nd.icode
LEFT JOIN patient p 
    ON o.hn = p.hn
WHERE oi.icode = '3003921'
  AND o.vstdate BETWEEN '2025-01-01' AND '2025-06-16'
ORDER BY o.vstdate, o.vsttime;
