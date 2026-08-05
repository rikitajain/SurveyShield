# ===========================
# Standard Library
# ===========================
import json

# ===========================
# Third Party Libraries
# ===========================
from fastapi import FastAPI, Depends, Request
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

# ===========================
# Database
# ===========================
from app.database.db import engine, get_db
from app.database import models
from app.database import audit_models
from app.database import rule_models

# ===========================
# API Models
# ===========================
from app.models.respondent import Respondent
from app.models.rule import Rule

# ===========================
# LOGGER for errors
# ===========================

from app.logger.logger import logger
from fastapi import Request

from app.exceptions.handlers import global_exception_handler

# ===========================
# Fraud Engines
# ===========================
from app.engine.email_engine import check_email
from app.engine.ip_engine import check_ip
from app.engine.device_engine import check_device
from app.engine.risk_engine import calculate_risk
from app.engine.decision_engine import get_decision
from app.engine.geo_engine import get_ip_location

# ===========================
# Database CRUD
# ===========================
from app.database.crud import create_respondent
from app.database.audit_crud import (
    create_audit_log,
    get_all_audit_logs,
)

from app.database.dashboard_crud import get_dashboard_summary

from app.database.rule_crud import (
    create_rule,
    get_rules,
)

# ===========================
# Routes
# ===========================

from app.routes.respondent_routes import router as respondent_router
from app.routes.dashboard_routes import router as dashboard_router
from app.routes.audit_routes import router as audit_router
from app.routes.rules_routes import router as rules_router
from app.routes.health_routes import router as health_router
from app.routes.dev_routes import router as dev_router

# ======================================
# Application Configuration
# ======================================
app = FastAPI(
    title="SurveyShield API",
    version="0.4.0",
    description="""
SurveyShield is an intelligent fraud detection platform
designed to identify duplicate and suspicious respondents
using configurable fraud detection engines.

Features

• Email Duplicate Detection
• IP Duplicate Detection
• Device Duplicate Detection
• Dynamic Rule Engine
• Audit Logging
• Dashboard Analytics
""",
)

app.add_exception_handler(
    Exception,
    global_exception_handler,
)

logger.info("SurveyShield Application Started")

app.include_router(respondent_router)
app.include_router(dashboard_router)
app.include_router(audit_router)
app.include_router(rules_router)
app.include_router(health_router)
app.include_router(dev_router)

# ======================================
# Static Files
# ======================================
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# ======================================
# Database Initialization
# ======================================

models.Base.metadata.create_all(bind=engine)
audit_models.Base.metadata.create_all(bind=engine)
rule_models.Base.metadata.create_all(bind=engine)