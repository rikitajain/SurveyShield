#Respondent Table

id
project_id
email
ip
country
browser
device_id
created_at

#Audit Log

id
project_id
email
ip
device_id
risk_score
decision
engine_results
timestamp

#Rules

id
project_id
engine
score
action

# Database Schema

## Overview

SurveyShield currently uses SQLite as its primary database.

The database stores respondents, audit logs, and fraud rules.

---

# Tables

## 1. Respondent

Purpose

Stores accepted respondents.

| Column | Type | Description |
|---------|------|-------------|
| id | Integer | Primary Key |
| project_id | String | Project Identifier |
| email | String | Respondent Email |
| ip | String | Client IP Address |
| country | String | Respondent Country |
| browser | String | Browser Information |
| device_id | String | Device Fingerprint |
| created_at | DateTime | Record Creation Time |

---

## 2. AuditLog

Purpose

Stores every fraud detection decision.

| Column | Type | Description |
|---------|------|-------------|
| id | Integer | Primary Key |
| project_id | String | Project Identifier |
| email | String | Respondent Email |
| ip | String | Client IP |
| device_id | String | Device Fingerprint |
| risk_score | Integer | Fraud Score |
| decision | String | ACCEPT / REVIEW / REJECT |
| engine_results | Text | Fraud Engine Results (JSON) |
| created_at | DateTime | Timestamp |

---

## 3. Rules

Purpose

Stores configurable fraud rules.

| Column | Type | Description |
|---------|------|-------------|
| id | Integer | Primary Key |
| project_id | String | Project Identifier |
| engine | String | Fraud Engine |
| score | Integer | Risk Score |
| action | String | ACCEPT / REVIEW / REJECT |

---

# Relationships

Project

│

├── Respondents

├── Audit Logs

└── Rules

---

# Future Tables

Planned for Version 1.0

- Projects
- Users
- Vendors
- Sessions
- Device History
- Geo History
- VPN Intelligence
- Proxy Intelligence