# Base URL

Development

http://127.0.0.1:8000

Production

(To be updated)

# SurveyShield API Documentation

---

# 1. Check Respondent

### Endpoint

POST /api/respondent/check

### Purpose

Checks whether a respondent is fraudulent before allowing them into the survey.

### Request

```json
{
    "project_id": "PROJECT_B",
    "uuid": "UUID001",
    "vendor": "Dynata",
    "country": "India",
    "browser": "...",
    "device_id": "...",
    "latitude": 28.61,
    "longitude": 77.23
}
```

### Response

```json
{
    "decision": "ACCEPT",
    "risk_score": 0,
    "engines": [],
    "reasons": []
}
```

---

# 2. Dashboard Summary

### Endpoint

GET /api/dashboard

### Purpose

Returns dashboard statistics.

### Request

No parameters

### Response

```json
{
    "total_respondents": 25,
    "accepted": 6,
    "review": 14,
    "rejected": 5
}
```

---

# 3. Audit Logs

### Endpoint

GET /api/audit

### Purpose

Returns all audit logs.

### Request

No parameters

### Response

```json
[
   {
      "id": 1,
      "decision": "ACCEPT",
      "risk_score": 0
   }
]
```

---

# 4. Add Rule

### Endpoint

POST /api/rules

### Purpose

Creates a fraud detection rule.

### Request

```json
{
    "project_id": "PROJECT_B",
    "engine": "IP",
    "score": 40,
    "action": "REVIEW"
}
```

### Response

```json
{
    "message": "Rule Created Successfully"
}
```

---

# 5. List Rules

### Endpoint

GET /api/rules/{project_id}

### Purpose

Returns all fraud rules for a project.

### Request

Example

```
GET /api/rules/PROJECT_B
```

### Response

```json
[
   {
      "engine": "IP",
      "score": 40,
      "action": "REVIEW"
   }
]
```

| API                           | Purpose           |
| ----------------------------- | ----------------- |
| POST `/api/respondent/check`  | Fraud Detection   |
| GET `/api/dashboard`          | Dashboard Summary |
| GET `/api/audit`              | Audit Logs        |
| POST `/api/rules`             | Add Rule          |
| GET `/api/rules/{project_id}` | List Rules        |
