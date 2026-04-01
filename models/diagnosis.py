from pydantic import BaseModel
from typing import Optional

class SymptomInput(BaseModel):
    symptoms: str

class DiagnosisRecord(BaseModel):
    symptoms: str
    result: dict