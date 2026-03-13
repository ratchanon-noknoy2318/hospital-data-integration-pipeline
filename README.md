# HOSxP Analytics Pipeline
**High-performance SQL architecture and ETL pipelines for legacy healthcare database systems.**

## Overview
This enterprise-grade data pipeline reverse-engineers undocumented HOSxP clinical data schemas to enable real-time, cross-department analytics. By refactoring legacy systems and optimizing MySQL database queries for over 400,000 patient records, the architecture achieves a significant reduction in data retrieval latency (from 24 hours to approximately 1 hour). This ensures rapid medical decision support within a strictly PDPA-compliant infrastructure.

## Architecture

| Layer | Description |
| :--- | :--- |
| **Pattern** | Dual-Channel ETL Data Pipeline |
| **Data Flow** | [Legacy HOSxP MySQL] -> [Python Orchestrator] -> [Optimized SQL Analytics] -> [BI Dashboard] |
| **Core Focus** | Legacy Refactoring, High-Concurrency Optimization, Role-Based Access Control (RBAC) |

## Tech Stack

| Component | Technology |
| :--- | :--- |
| **Data Processing** | Python (Pandas) |
| **Database** | MySQL (HOSxP) |
| **Infrastructure** | PDPA-Compliant Secure Environment |

## Project Structure

| Directory | Description |
| :--- | :--- |
| `Database/` | Schema definitions and structural data models. |
| `Python/` | Core ETL scripts, automation, and data processing logic. |
| `SQL/` | Optimized queries for analytics and high-speed data extraction. |

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
