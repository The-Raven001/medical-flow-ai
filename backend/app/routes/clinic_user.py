from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy import or_
from sqlalchemy.orm import Session
from app.schemas import schemas
from app.models import clinic_user_models as models
from app.utils.password_verification import hash_password, verify_password


router = APIRouter(prefix="/clinic_users", tags=["Clinic_Users"])

#Create user for medical provider

@router.post("/",
    response_model=schemas.ClinicUserResponse,
    status_code=201,
    summary="Create a new clinic user",
    description="Create a new user with access from the side of clinic to help with administrative tasks."
    )
def create_clinic_user(user: schemas.ClinicUserCreate, db: Session = Depends(get_db)):

    existing_user = (
        db.query(models.ClinicUser).filter(or_(models.ClinicUser.email == user.email, models.ClinicUser.username == user.username)).first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered or username already in use"
        )



    hashed_password = hash_password(user.password)
    new_clinic_user = models.ClinicUser(username=user.username, first_name=user.first_name, last_name=user.last_name, email=user.email, hashed_password=hashed_password)
    db.add(new_clinic_user)
    db.commit()
    db.refresh(new_clinic_user)
    return new_clinic_user