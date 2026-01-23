SELECT
    o.hn,
    o.agent,
    o.symptom,
    o.begin_date,
    CONCAT(p.pname, p.fname, ' ', p.lname) AS patient_name,
    ar.relation_name,
    ag.allergy_group_name,
    asr.seriousness_name,
    ars.result_name,
    sp.name AS spclty_name
FROM opd_allergy o
LEFT OUTER JOIN patient p ON p.hn = o.hn
LEFT OUTER JOIN allergy_group ag ON ag.allergy_group_id = o.allergy_group_id
LEFT OUTER JOIN allergy_seriousness asr ON asr.seriousness_id = o.seriousness_id
LEFT OUTER JOIN allergy_result ars ON ars.allergy_result_id = o.allergy_result_id
LEFT OUTER JOIN allergy_relation ar ON ar.allergy_relation_id = o.allergy_relation_id
LEFT OUTER JOIN spclty sp ON sp.spclty = o.spclty;
