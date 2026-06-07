from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import List, Optional
from datetime import datetime

class IntakeBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, example="New patient notes")
    description: str = Field(max_length=2000, example="Patient has asthma, difficulty breathing and nasal congestion.")

class Intake(IntakeBase):
    id: int
    patient_id: int
    created_at: datetime


class IntakeUpdate(IntakeBase):
    title: Optional[str] = None
    description: Optional[str]= None
    last_edited: datetime