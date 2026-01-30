SELECT
    o.hn,
    o.agent,
    o.symptom,
    o.begin_date,
    CONCAT(p.pname, p.fname, ' ', p.lname) AS patient_name,
    ar.relation_name,
    ag.allergy_group_name,
    srs.seriousness_name,
    arl.result_name,
    sp.name AS spclty_name
FROM opd_allergy o
LEFT JOIN patient p
    ON p.hn = o.hn
LEFT JOIN allergy_group ag
    ON ag.allergy_group_id = o.allergy_group_id
LEFT JOIN allergy_seriousness srs
    ON srs.seriousness_id = o.seriousness_id
LEFT JOIN allergy_result arl
    ON arl.allergy_result_id = o.allergy_result_id
LEFT JOIN allergy_relation ar
    ON ar.allergy_relation_id = o.allergy_relation_id
LEFT JOIN spclty sp
    ON sp.spclty = o.spclty;
