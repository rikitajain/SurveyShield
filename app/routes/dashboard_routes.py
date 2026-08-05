from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.database.dashboard_crud import get_dashboard_summary

router = APIRouter(
    tags=["Dashboard"]
)

@router.get(
    "/api/dashboard",
    summary="Dashboard Summary"
)
def dashboard(
    db: Session = Depends(get_db)
):
   return get_dashboard_summary(db)