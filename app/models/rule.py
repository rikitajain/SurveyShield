from pydantic import BaseModel


class Rule(BaseModel):
    project_id: str
    engine: str

    enabled: bool

    score: int

    severity: str

    action: str

    reason: str

    description: str