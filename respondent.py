from pydantic import BaseModel


class Respondent(BaseModel):
    email: str
    ip: str
    country: str
    browser: str
    device_id: str