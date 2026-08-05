from sqlalchemy import Column, Integer, String, Boolean

from app.database.db import Base

class ProjectRule(Base):

    __tablename__ = "project_rules"

    id = Column(Integer, primary_key=True, index=True)

    project_id = Column(String, index=True)

    engine = Column(String)

    enabled = Column(Boolean, default=True)

    score = Column(Integer)

    severity = Column(String)

    action = Column(String)

    reason = Column(String)

    description = Column(String)