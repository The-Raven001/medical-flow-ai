from pydantic import BaseModel, EmailStr, Field

class ClinicUserBase(BaseModel):
    username: str = Field(..., example="user123")
    email: EmailStr = Field(..., example="useremail@example.com")
    name: str = Field(..., example="Carlos")
    lastName: str = Field(..., example="Gonzalez")

class ClinicUserCreate(ClinicUserBase):
    password: str = Field(..., example="12345")

class ClinicUser(ClinicUserBase):
    id: int
    patients: List[] = Field(default_factory=list)
    #fix this!

    class Config:
        orm_mode = True

class ClinicUserLogin(BaseModel):
    email: EmailStr = Field(..., example= "useremail@example.com")
    password: str = Field(..., example="12345")

class Token(BaseModel):
    access_token: str = Field(..., example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnYWNtOTUyMThAZ21haWwuY29t")
    token_type: str = Field(..., example="bearer")
