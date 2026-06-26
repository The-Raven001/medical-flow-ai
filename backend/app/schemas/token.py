from pydantic import BaseModel, Field

class Token(BaseModel):
    access_token: str = Field(..., example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnYWNtOTUyMThAZ21haWwuY29tIiwiZXhwIjoxNzY2NzE5NjE1fQ.QtDC5RHSYF5u3QcC_QSHz3fk7n2BBwcZB9J_lEEJQEE")
    token_type: str = Field(..., example="bearer")

class LoginRequest(BaseModel):
    username: str = Field(..., example="Raven")
    password: str = Field(..., example="1234567890")