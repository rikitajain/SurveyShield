from pydantic import BaseModel


class EngineResult(BaseModel):
    engine: str
    matched: bool
    score: int
    severity: str
    reason: str