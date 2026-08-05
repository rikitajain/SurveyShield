from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {
        "product": "SurveyShield",
        "version": "0.2.0",
        "status": "Running"
    }