from typing import Optional

from pydantic import BaseModel


class Respondent(BaseModel):

    project_id: str

    uuid: Optional[str] = None

    vendor: Optional[str] = None

    email: Optional[str] = None

    ip: str = ""

    country: str = ""

    browser: str = ""

    device_id: str = ""

    latitude: Optional[float] = None

    longitude: Optional[float] = None