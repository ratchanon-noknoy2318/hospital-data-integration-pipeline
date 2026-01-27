# HOSxP Data Integration Pipeline
### Kamphaeng Phet Municipality Community Hospital

**Project Impact:** Optimized SQL architecture for **400,000+ patient records**, utilizing AI-driven auditing and high-performance SQL engineering to support executive strategic planning.

---

### 1. Systematic Data Pipeline Structure

| Operational Layer | Technical Implementation (SQL) | AI & Data Logic | Organizational Impact |
| :--- | :--- | :--- | :--- |
| **Executive Layer** | Complex Analytical Views & Strategic Queries | Pattern Trend Analysis | **Top-Level Management** data accessibility for policy making. |
| **Audit Layer** | SQL Validation Scripts & Master Data MDM | AI Anomaly & Age-Mismatch Detection | Identified complex errors missed by standard SQL filters. |
| **Automation Layer** | Stored Procedures & Database Triggers | Real-time Integration Triggers | Reduced administrative overhead and improved response times. |
| **Security Layer** | HN Primary Key & PII Minimization | PDPA Compliance Protocols | Secured **400K+ records** against duplication & leakage. |

---

### 2. Database Schema Architecture (Patient Master)

| Field Name | Data Type | SQL Constraint | PDPA/Functional Role |
| :--- | :--- | :--- | :--- |
| **hn** | **VARCHAR(10)** | **PRIMARY KEY** | **Internal Hospital Reference (Unique)** |
| citizen_id | VARCHAR(13) | UNIQUE / NOT NULL | PII - Identity Verification |
| title | VARCHAR(20) | NOT NULL | Identity - Name Prefix |
| first_name | VARCHAR(100) | NOT NULL | Identity - Patient Given Name |
| last_name | VARCHAR(100) | NOT NULL | Identity - Patient Surname |
| birthdate | DATE | NOT NULL | Sensitive - Logic for AI Age-Validation |
| gender | INT | CHECK (1,2) | Demographic Analysis |
| house_number | VARCHAR(50) | - | Location - Household Logistics |
| road | VARCHAR(100) | - | Location - Infrastructure Planning |
| village_name | VARCHAR(100) | - | Location - Geospatial Resource Allocation |

---

### 3. Core Technical Competencies
* **Environment:** HOSxP Production Database (MySQL/MariaDB)
* **Language:** Advanced SQL (DML, DDL, DCL)
* **Framework:** Data Governance & Master Data Management (MDM)

---

### 4. Contact Information
* **Lead Engineer:** Ratchanon Noknoy
* **LinkedIn:** [linkedin.com/in/ratchanon-noknoy/](https://linkedin.com/in/ratchanon-noknoy/)
* **GitHub:** [github.com/ratchanon-noknoy2318](https://github.com/ratchanon-noknoy2318)
* **Email:** ratchanon.noknoy2318@gmail.com
