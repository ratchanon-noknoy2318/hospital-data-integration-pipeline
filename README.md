# HOSxP Data Integration Pipeline
**Kamphaeng Phet Municipality Community Hospital**

A production-oriented SQL data integration and governance pipeline for HOSxP hospital systems, explicitly designed with **AI-assisted analytics and data validation** to support clinical reporting, auditing, and secure patient master data management at scale.

---

## 1. Data Scale & Infrastructure

| Metric | Specification | Technical Detail |
| :--- | :--- | :--- |
| **Data Volume** | **400,000+ Records** | Patient Master Data Management (MDM) |
| **Database Engine** | MySQL / MariaDB | HOSxP Production Environment |
| **Query Optimization** | Indexed & Tuned SQL | High-Concurrency OPD/IPD Access |
| **Regulatory Compliance** | PDPA (Thailand) | SQL-Level Data Masking & Minimization |

---

## 2. Pipeline Architecture with AI Analytics

| Layer | Implementation | AI Utilization | Business Impact |
| :--- | :--- | :--- | :--- |
| **Analytics** | SQL Views / Data Marts | AI-assisted pattern and trend analysis | Evidence-based decision support |
| **Auditing** | Validation Queries | AI-driven anomaly and outlier detection | Improved data quality assurance |
| **Automation** | Stored Procedures | Rule-based logic with AI insights | Reduced operational workload |
| **Security** | PK / FK Constraints | AI-supported consistency checks | Secure and compliant patient data |

---

## 3. Core Database Schema (Patient Master)

| Field | Type / Constraint | Description |
| :--- | :--- | :--- |
| **hn** | **VARCHAR(10) [PK]** | Primary Hospital Identifier |
| **citizen_id** | VARCHAR(13) [UNIQUE] | National Identity Verification |
| **full_name** | VARCHAR(200) | Patient Identification |
| **birthdate** | DATE | AI-based age validation and consistency checks |
| **location** | TEXT | Geographic and service area analytics |

---

## 4. Key Features

- AI-assisted analytics for population health and service utilization
- AI-supported data validation and anomaly detection
- Designed for real HOSxP production databases
- Optimized SQL for large-scale hospital data
- Built-in PDPA-aware masking and data minimization
- Suitable for reporting, integration, auditing, and AI-driven insights
- Ready for extension into ETL, BI, and advanced AI pipelines

---

## 5. Maintainer & Contact

| Role | Reference |
| :--- | :--- |
| **Lead Engineer** | Ratchanon Noknoy |
| **Portfolio** | https://ratchanon-portfolio.vercel.app/ |
| **Profiles** | LinkedIn: https://linkedin.com/in/ratchanon-noknoy/  
| | GitHub: https://github.com/ratchanon-noknoy2318 |
| **Email** | ratchanon.noknoy2318@gmail.com |
