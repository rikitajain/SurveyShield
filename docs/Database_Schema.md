# Database Schema

**Version:** 1.1  
**Database:** SQLite  
**Last Updated:** 06-Aug-2026

---

## Overview

SurveyShield currently uses **SQLite** as its primary database.

The database stores respondent information, fraud detection audit logs, and configurable fraud detection rules.

---

## Current Tables

| Table | Purpose |
|--------|----------|
| Respondent | Stores accepted respondents |
| AuditLog | Stores fraud detection history |
| Rules | Stores configurable fraud rules |

---

# Tables

## 1. Respondent

### Purpose

Stores accepted respondents after they successfully pass the SurveyShield fraud detection engine.

### Columns

| Column | Type | Description |
|---------|------|-------------|
| id | Integer | Primary Key |
| project_id | String | Project Identifier |
| uuid | String | Unique Respondent Identifier |
| vendor | String | Sample Provider / Vendor Name |
| email | String | Respondent Email |
| ip | String | Client IP Address |
| country | String | Respondent Country |
| browser | String | Browser Information |
| device_id | String | Browser Device Fingerprint |
| latitude | Float | GPS Latitude |
| longitude | Float | GPS Longitude |
| location_permission | String | Browser Location Permission (Granted / Denied / Unavailable / Timeout) |
| location_accuracy | Float | GPS Accuracy (Meters) |
| created_at | DateTime | Record Creation Timestamp |

---

### Example Record

| Field | Value |
|--------|-------|
| project_id | PROJECT_B |
| uuid | UUID001 |
| vendor | Dynata |
| ip | 127.0.0.1 |
| country | India |
| latitude | -26.0253995 |
| longitude | 28.036299 |
| location_permission | Granted |
| location_accuracy | 55 |
| created_at | 2026-08-06 13:19:09 |

---

### Notes

- GPS coordinates are collected only when the respondent grants browser location permission.
- GPS accuracy is stored in meters as reported by the browser.
- Device ID is generated using browser fingerprinting.
- Respondent records are stored only after successfully passing the SurveyShield fraud detection engine.

---

## 2. AuditLog

### Purpose

Stores every fraud detection request and its evaluation results for auditing, monitoring, and investigation.

### Columns

| Column | Type | Description |
|---------|------|-------------|
| id | Integer | Primary Key |
| project_id | String | Project Identifier |
| email | String | Respondent Email |
| ip | String | Client IP Address |
| device_id | String | Browser Device Fingerprint |
| risk_score | Integer | Calculated Fraud Risk Score |
| decision | String | ACCEPT / REVIEW / REJECT |
| engine_results | Text | JSON output from all fraud engines |
| created_at | DateTime | Audit Timestamp |

---

### Example Record

| Field | Value |
|--------|-------|
| project_id | PROJECT_B |
| email | user@example.com |
| ip | 127.0.0.1 |
| device_id | TW96aWxsYS... |
| risk_score | 15 |
| decision | ACCEPT |
| engine_results | {"duplicate_email":false,"device_match":false} |
| created_at | 2026-08-06 13:19:09 |

---

## 3. Rules

### Purpose

Stores configurable fraud detection rules and their associated risk scores.

### Columns

| Column | Type | Description |
|---------|------|-------------|
| id | Integer | Primary Key |
| project_id | String | Project Identifier |
| engine | String | Fraud Detection Engine Name |
| score | Integer | Risk Score Assigned |
| action | String | ACCEPT / REVIEW / REJECT |

---

### Example Record

| Field | Value |
|--------|-------|
| project_id | PROJECT_B |
| engine | Country Validation |
| score | 40 |
| action | REVIEW |

---

# Database Relationships

```text
Project
│
├── Respondents
├── Audit Logs
└── Rules
```

---

## Future Tables (Planned for v2.0+)

The following tables are planned as SurveyShield evolves into a complete fraud detection platform.

- Projects
- Users
- Vendors
- Sessions
- Device History
- Geo History
- VPN Intelligence
- Proxy Intelligence
- Browser Intelligence
- Fingerprint History
- Risk Profiles
- Fraud Reports

---

## Database Design Principles

- Store only validated respondent records.
- Maintain a complete audit trail for every fraud evaluation.
- Keep fraud rules configurable without changing application code.
- Support future scalability by separating operational and historical data.
- Ensure all fraud engine outputs are traceable for debugging and compliance.

---

**Document Version:** 1.1

**Maintained By:** Rikita Jain

**Project:** SurveyShield