from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime

from app.database.db import Base


class RespondentDB(Base):
    __tablename__ = "respondents"

    id = Column(Integer, primary_key=True, index=True)

    project_id = Column(String, index=True)

    uuid = Column(String)

    vendor = Column(String)

    email = Column(String)

    ip = Column(String)

    country = Column(String)

    browser = Column(String)

    device_id = Column(String)

    latitude = Column(Float)

    longitude = Column(Float)

    location_permission = Column(String)

    location_accuracy = Column(Float)

    created_at = Column(DateTime, default=datetime.utcnow)