from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas import schemas
from app.models import
from app.utils.password_verification import hash, verify


router = APIRouter(prefix="/providers", tags=["Providers"])

#Create user for medical provider

@router.post("/",
    response_model=schemas.ClinicUser,
    status_code=201,
    summary="Create a new clinic user"
    description="Create a new user with access from the side of clinic to help with administrative tasks."
    )
def create_clinic_user(user: schemas.ClinicUser, db: Session = Depends(get_db)):
    hashed_password = has(user.password)
    new_clinic_user = models.ClinicUser(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(new_clinic_user)
    db.commit()
    db.refresh(new_user)
    return new_clinic_user