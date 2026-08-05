# SurveyShield Architecture

## Overview

SurveyShield is a real-time fraud prevention platform for online survey research.

It consists of four major layers.

```
Survey Platform
(Decipher / STG / Qualtrics)

            │

SurveyShield SDK
(JavaScript)

            │

REST API
(FastAPI)

            │

Fraud Detection Engines

            │

Risk Engine

            │

Decision Engine

            │

SQLite Database

            │

Dashboard APIs

            │

Future Dashboard UI
```

---

## Components

### JavaScript SDK

Responsible for

- Browser detection
- Device fingerprint generation
- GPS capture
- Survey metadata
- API communication

---

### FastAPI Backend

Receives requests from SDK.

Runs fraud engines.

Returns decision.

---

### Fraud Engines

Current

- Email Engine
- IP Engine
- Device Engine

Future

- VPN Engine
- Proxy Engine
- ASN Engine
- Geo Engine
- Velocity Engine

---

### Risk Engine

Combines all fraud engine scores.

Produces

```
Risk Score
```

---

### Decision Engine

Maps risk score into

- ACCEPT
- REVIEW
- REJECT

---

### Database

Stores

- Respondents
- Audit Logs
- Rules

---

### Dashboard

Provides

- Total Respondents
- Accepted
- Review
- Rejected