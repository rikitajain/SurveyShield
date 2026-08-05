from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database.db import get_db

router = APIRouter(
    tags=["Developer"]
)


@router.get("/tables")
def get_tables(
    db: Session = Depends(get_db)
):

    result = db.execute(
        text("SELECT name FROM sqlite_master WHERE type='table'")
    )

    tables = [row[0] for row in result]

    return {
        "tables": tables
    }