from pydantic import BaseModel, EmailStr, Field
from app.schemas import PatientSummary
from typing import List

class ClinicUserBase(BaseModel):
    username: str = Field(..., example="user123")
    email: EmailStr = Field(..., example="useremail@example.com")
    first_name: str = Field(..., example="Carlos")
    last_name: str = Field(..., example="Gonzalez")

class ClinicUserCreate(ClinicUserBase):
    password: str = Field(..., example="12345")

class ClinicUserResponse(ClinicUserBase):
    id: int
    patients: List[PatientSummary] = Field(default_factory=list)

    class Config:
        orm_mode = True

class ClinicUserLogin(BaseModel):
    email: EmailStr = Field(..., example= "useremail@example.com")
    password: str = Field(..., example="12345")

class Token(BaseModel):
    access_token: str = Field(..., example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnYWNtOTUyMThAZ21haWwuY29t")
    token_type: str = Field(..., example="bearer")
