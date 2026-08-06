from sqlalchemy.orm import Session
from app.database.models import RespondentDB


def get_respondent_by_email(
    db: Session,
    project_id: str,
    email: str
):

    return (
        db.query(RespondentDB)
        .filter(
            RespondentDB.project_id == project_id,
            RespondentDB.email == email
        )
        .first()
    )

def get_respondent_by_ip(
    db: Session,
    project_id: str,
    ip: str
):

    return (
        db.query(RespondentDB)
        .filter(
            RespondentDB.project_id == project_id,
            RespondentDB.ip == ip
        )
        .first()
    )

def get_respondent_by_device(
    db: Session,
    project_id: str,
    device_id: str
):

    return (
        db.query(RespondentDB)
        .filter(
            RespondentDB.project_id == project_id,
            RespondentDB.device_id == device_id
        )
        .first()
    )

def count_device_usage(
    db: Session,
    project_id: str,
    device_id: str,
):

    return (
        db.query(RespondentDB)
        .filter(
            RespondentDB.project_id == project_id,
            RespondentDB.device_id == device_id,
        )
        .count()
    )
    
def create_respondent(
    db: Session,
    project_id,
    uuid,
    vendor,
    email,
    ip,
    country,
    browser,
    device_id,
    latitude,
    longitude,
    location_permission,
    location_accuracy,
):

    respondent = RespondentDB(
        project_id=project_id,
        uuid=uuid,
        vendor=vendor,
        email=email,
        ip=ip,
        country=country,
        browser=browser,
        device_id=device_id,
        latitude=latitude,
        longitude=longitude,
        location_permission=location_permission,
        location_accuracy=location_accuracy,
    )

    db.add(respondent)

    db.commit()

    db.refresh(respondent)

    return respondent