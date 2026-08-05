# SurveyShield

**Version:** 0.2.0

**Status:** Under Active Development

**Author:** Rikita Jain

---

# Overview

SurveyShield is a fraud prevention platform designed for online survey research. It detects duplicate and suspicious respondents before they complete a survey, helping research agencies improve data quality and reduce fraudulent responses.

SurveyShield integrates seamlessly with survey platforms such as **Decipher** through a lightweight JavaScript SDK and performs real-time fraud detection using multiple validation engines.

---

# Vision

To become a comprehensive fraud prevention platform for online market research by combining browser intelligence, device fingerprinting, IP intelligence, geolocation, behavioral analytics, and customizable fraud rules.

---

# Current Features

### JavaScript SDK

* Browser fingerprint collection
* Device fingerprint generation
* Geolocation capture (with user permission)
* Survey metadata collection
* Secure communication with backend API

---

### Fraud Detection Engines

* Email Duplicate Detection
* IP Duplicate Detection
* Device Fingerprint Detection
* Risk Score Calculation
* Decision Engine (Accept / Review / Reject)

---

### Backend

* FastAPI
* SQLite Database
* SQLAlchemy ORM
* REST APIs
* Audit Logging

---

### Dashboard APIs

* Total Respondents
* Accepted Respondents
* Review Respondents
* Rejected Respondents

---

# Current Architecture

```
Survey Platform (Decipher)

        │

SurveyShield SDK (JavaScript)

        │

FastAPI Backend

        │

Fraud Detection Engines

        │

Risk Engine

        │

Decision Engine

        │

SQLite Database

        │

Dashboard API
```

---

# Technology Stack

Frontend SDK

* JavaScript

Backend

* FastAPI
* Python 3

Database

* SQLite
* SQLAlchemy

Development Tools

* VS Code
* Git (Planned)

---

# Folder Structure

```
SurveyShield/

app/
    database/
    engine/
    models/

sdk/
    surveyshield.js

static/
    test.html

docs/

main.py

requirements.txt
```

---

# APIs

Current APIs

* POST /api/respondent/check
* GET /api/audit
* GET /api/dashboard
* POST /api/rules
* GET /api/rules/{project_id}

---

# Current Version

Version 0.2

Completed

✔ FastAPI Backend

✔ JavaScript SDK

✔ Device Fingerprinting

✔ Browser Detection

✔ Backend IP Detection

✔ GPS Capture

✔ Fraud Detection Engines

✔ Audit Logging

✔ Dashboard Summary API

---

# Planned Features

Version 0.3

* Project Cleanup
* Documentation
* Improved Folder Structure

Version 0.4

* Decipher Integration

Version 0.5

* Dashboard User Interface

Version 0.6

* VPN Detection
* Proxy Detection
* ASN Detection
* Datacenter Detection

Version 0.7

* Rule Builder

Version 0.8

* Reports & Export

Version 0.9

* User Management

Version 1.0

* Production Release
* Enterprise Dashboard
* Multi-Project Support
* Client Demonstration Ready

---

# License

Internal Development Project

Confidential
