from Pydantic import BaseModel, EmailStr, Field

class PatientBase(BaseModel):
    email: EmailStr = Field(..., example="useremail@example.com")
    name: str = Field(..., example="Carlos")
    lastName: str = Field(...., example="Gonzalez")
    chart: int


class PatientSummary(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        from_attributes = True

