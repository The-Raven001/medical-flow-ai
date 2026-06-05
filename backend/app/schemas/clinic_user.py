from pydantic import BaseModel, EmailStr, Field, ConfigDict
from app.schemas.patients import PatientSummary
from typing import List

class ClinicUserBase(BaseModel):
    username: str = Field(..., example="user123")
    email: EmailStr = Field(..., example="useremail@example.com")
    first_name: str = Field(..., example="Carlos")
    last_name: str = Field(..., example="Gonzalez")

class ClinicUserCreate(ClinicUserBase):
    password: str = Field(..., min_length=8, example="12345")

class ClinicUserResponse(ClinicUserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

        

class ClinicUserLogin(BaseModel):
    email: EmailStr = Field(..., example= "useremail@example.com")
    password: str = Field(..., min_length=8, example="12345")

class Token(BaseModel):
    access_token: str = Field(..., example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnYWNtOTUyMThAZ21haWwuY29t")
    token_type: str = Field(..., example="bearer")
