from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.routes.clinic_users import router as clinic_users
from app.routes.intakes import router as intake
from app.routes.patients import router as patients  
from app.database import engine, Base, get_db
from app.models.clinic_users import ClinicUsers
import app.schemas.clinic_users as schemas
from app.schemas.token import Token
from app.routes.auth import create_access_token, get_current_user
from app.utils.password_verification import hash_password, verify_password

import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(clinic_users)
app.include_router(intake)
app.include_router(patients)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Backend running"}

@app.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(ClinicUsers).filter(ClinicUsers.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/me", response_model=schemas.ClinicUsersResponse)
async def read_me(current_user: ClinicUsers = Depends(get_current_user)):
    return current_user
    

