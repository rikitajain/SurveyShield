# 🛡️ SurveyShield

SurveyShield is a FastAPI-based fraud detection platform designed to identify suspicious survey respondents using configurable fraud detection engines. The application evaluates respondents against multiple rules, calculates a risk score, and determines whether a respondent should be **Accepted**, **Reviewed**, or **Rejected**.

---

# 🚀 Features

* Duplicate Email Detection
* Duplicate IP Detection
* Duplicate Device Detection
* Configurable Rule Engine
* Risk Score Calculation
* Decision Engine (Accept / Review / Reject)
* Audit Logging
* Dashboard Summary API
* Geo-IP Lookup
* REST APIs using FastAPI
* SQLAlchemy Database Integration
* Unit & API Testing using Pytest

---

# 🏗️ Tech Stack

* Python 3.13
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Pytest
* Uvicorn

---

# 📂 Project Structure

```text
SurveyShield/
│
├── app/
│   ├── api/
│   │   ├── respondent_routes.py
│   │   ├── dashboard_routes.py
│   │   ├── audit_routes.py
│   │   └── rule_routes.py
│   │
│   ├── database/
│   │   ├── db.py
│   │   ├── crud.py
│   │   ├── audit_crud.py
│   │   ├── dashboard_crud.py
│   │   ├── rule_crud.py
│   │   ├── models.py
│   │   ├── audit_models.py
│   │   └── rule_models.py
│   │
│   ├── engine/
│   │   ├── email_engine.py
│   │   ├── ip_engine.py
│   │   ├── device_engine.py
│   │   ├── rule_helper.py
│   │   ├── risk_engine.py
│   │   ├── decision_engine.py
│   │   ├── geo_engine.py
│   │   └── engines.py
│   │
│   ├── models/
│   │   ├── respondent.py
│   │   └── rule.py
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   └── main.py
│
├── tests/
│   ├── test_api.py
│   ├── test_decision_engine.py
│   ├── test_email_engine.py
│   ├── test_ip_engine.py
│   ├── test_device_engine.py
│   └── test_risk_engine.py
│
├── surveyshield.db
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# ⚙️ Fraud Detection Workflow

1. Receive respondent details.
2. Detect client IP.
3. Fetch Geo-IP information.
4. Execute all enabled fraud engines.
5. Calculate cumulative risk score.
6. Determine decision:

   * ACCEPT
   * REVIEW
   * REJECT
7. Store audit log.
8. Save respondent if accepted.
9. Return fraud analysis to the client.

---

# 📊 Current Fraud Engines

| Engine        | Purpose                          |
| ------------- | -------------------------------- |
| Email Engine  | Detect duplicate email addresses |
| IP Engine     | Detect duplicate IP addresses    |
| Device Engine | Detect duplicate device IDs      |

---

# 📈 Decision Logic

| Risk Score             | Decision |
| ---------------------- | -------- |
| Below Review Threshold | ACCEPT   |
| Review Threshold       | REVIEW   |
| Reject Threshold       | REJECT   |

Threshold values are configurable through application settings.

---

# 🧪 Running Tests

```bash
pytest
```

Current Status:

* 14 Tests Passing

---

# ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# 🛣️ Roadmap

### ✅ Phase 1 (Completed)

* Backend APIs
* Fraud Engines
* Rule Management
* Dashboard
* Audit Logs
* Unit Testing
* API Testing
* Code Refactoring
* Type Hints

### 🔄 Phase 2 (In Progress)

* Dedicated Test Database
* Browser Detection Engine
* Country Validation Engine
* Velocity Detection
* Disposable Email Detection

### 🔮 Phase 3 (Future)

* React Dashboard
* Authentication
* User Management
* Charts & Analytics
* Role-Based Access Control

### 🚀 Phase 4 (Vision)

* AI-powered Fraud Detection
* Machine Learning Risk Prediction
* Admin Portal
* Cloud Deployment

---

# 👨‍💻 Author

Developed by **Rikita Jain**

SurveyShield is being built as a learning-focused production-style backend project to explore fraud detection, API development, software architecture, testing, and clean coding practices using FastAPI.
