from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.clinic_users import ClinicUsers
from app.utils.password_verification import hash_password, verify_password
from app.utils.token import create_access_token, get_current_user
from app.schemas.token import LoginRequest, ChangePasswordRequest
from app.schemas.token import Token
from app.schemas.clinic_users import ClinicUsersResponse

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=Token)
async def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(ClinicUsers).filter(ClinicUsers.username == credentials.username).first()
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/change-password")
async def change_password(credentials: ChangePasswordRequest, db: Session = Depends(get_db), current_user: ClinicUsers = Depends(get_current_user)):
    if not verify_password(credentials.current_password, current_user.hashed_password):
        raise HTTPException(status_code=400, detail="Old password is incorrect")
    current_user.hashed_password = hash_password(credentials.new_password)
    db.commit()
    return {"message": "Password changed successfully"}

@router.get("/me", response_model=ClinicUsersResponse)
async def read_me(current_user: ClinicUsers = Depends(get_current_user)):
    return current_user
    