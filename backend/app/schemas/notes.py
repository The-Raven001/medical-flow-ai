from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class NotesBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, example="New patient note")
    content: str = Field(..., min_length=1, max_length=2500, example="Patient has been diagnosed with asthama and has been prescribed antibiotics")

class NotesCreate(NotesBase):
    patient_id: int
    clinic_user_id: int

class NotesResponse(NotesBase):
    id: int
    patient_id: int
    clinic_user_id: int
    created_at: datetime
    last_edited: datetime

    model_config = ConfigDict(from_attributer=True)

class NotesUpdate(NotesBase):
    title: Optional[str] = None
    content: Optional[str] = None
    clinic_user_id: int
    last_edited: datetime