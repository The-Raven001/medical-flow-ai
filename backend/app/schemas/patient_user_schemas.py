from Pydantic import BaseModel, EmailStr, Field

class PatientUserBase(BaseModel):
    email: EmailStr = Field(..., example="useremail@example.com")
    name: str = Field(..., example="Carlos")
    lastName: str = Field(...., example="Gonzalez")
    chart: int


