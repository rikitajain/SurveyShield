from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.db import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    project_id = Column(String, index=True)

    email = Column(String)

    ip = Column(String)

    device_id = Column(String)

    risk_score = Column(Integer)

    decision = Column(String)

    matched_engines = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)