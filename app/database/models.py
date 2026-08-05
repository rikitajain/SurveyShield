from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.db import Base

class RespondentDB(Base):
    __tablename__ = "respondents"

    id = Column(Integer, primary_key=True, index=True)

    project_id = Column(String, index=True)

    email = Column(String)
    ip = Column(String)
    country = Column(String)
    browser = Column(String)
    device_id = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)