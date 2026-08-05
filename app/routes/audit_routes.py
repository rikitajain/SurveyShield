from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.database.audit_crud import get_all_audit_logs

router = APIRouter(
    tags=["Audit"]
)

# ======================================
# Audit APIs
# ======================================

@router.get(
    "/api/audit",
    summary="Audit Logs"
)
def get_audit_logs(
    db: Session = Depends(get_db)
):

    logs = get_all_audit_logs(db)

    return logs
