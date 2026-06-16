from pydantic import BaseModel, EmailStr, Field, ConfigDict
from sqlalchemy.sql import func
from datetime import datetime

class PatientsBase(BaseModel):
    email: EmailStr = Field(..., example="useremail@example.com")
    first_name: str = Field(..., example="Carlos")
    last_name: str = Field(..., example="Gonzalez")
    date_of_birth: datetime
    phone_number: str = Field(..., example="+1 123456789")
    gender: str = Field(..., example="male")
    preferred_language: str = Field(..., example="Mandarin")
    intake_status: str = Field(..., example="pending")
    emergency_contact_name: str = Field(..., example="Luis Medina")
    emergency_contact_phone_number: str = Field(..., example="+13233233230")
    insurance_provider: str = Field(..., example="Anthem Blue Cross")
    insurance_id: str = Field(..., example="JQO123456789")
    chart: int



class PatientsSummary(BaseModel):
    id: int
    first_name: str
    last_name: str
    date_of_birth: datetime

    model_config = ConfigDict(from_attributes=True)

