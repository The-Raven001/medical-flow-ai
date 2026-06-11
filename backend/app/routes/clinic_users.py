from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy import or_
from sqlalchemy.orm import Session
from app.schemas import clinic_users as schemas
from app.models.clinic_users import ClinicUsers
from app.models.patients import Patients
from app.models.intakes import Intakes
from app.utils.password_verification import hash_password, verify_password


router = APIRouter(prefix="/clinic_users", tags=["Clinic_Users"])

#Create user for medical provider

@router.post("/",
    response_model=schemas.ClinicUsersResponse,
    status_code=201,
    summary="Create a new clinic user",
    description="Create a new user with access from the side of clinic to help with administrative tasks."
    )
def create_clinic_user(user: schemas.ClinicUsersCreate, db: Session = Depends(get_db)):

    existing_user = (
        db.query(ClinicUsers).filter(or_(ClinicUsers.email == user.email, ClinicUsers.username == user.username)).first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered or username already in use"
        )
    hashed_password = hash_password(user.password)
    new_clinic_user = ClinicUsers(username=user.username, first_name=user.first_name, last_name=user.last_name, email=user.email, hashed_password=hashed_password)
    db.add(new_clinic_user)
    db.commit()
    db.refresh(new_clinic_user)
    return new_clinic_user

#Retrieve users data all/individually

@router.get("/",
    response_model=schemas.ClinicUsersResponse,
    status_code=200,
    summary="Retrieve all users data",
    description="Request to retrieve all data of created users to current date."        
            )
def get_users(db: Session = Depends(get_db)):
    return db.query(ClinicUsers).all()

@router.get("/{id}",
    response_model=schemas.ClinicUsersResponse,
    status_code=200,
    summary="Retrieve a certain user",
    description="Retrieve the data of a certain user using their id as a filter.")
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(ClinicUsers).filter(ClinicUsers.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

#Update user data

@router.put("/{id}",
    response_model=schemas.ClinicUsersResponse,
    status_code=200,
    summary="Update data of speficied user",
    description="Update the name, last name, username, email, and or password of user."
    )
def update_user(id: int, updated_user: schemas.ClinicUsersCreate, db: Session = Depends(get_db)):
    user = db.query(ClinicUsers).filter(ClinicUsers.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    hashed_password = hash_password(updated_user.password)

#You might want to add if statements here to check if the email or username exists in the database
#already as it might throw an error given that those two are unique.

    user.username = updated_user.username
    user.email = updated_user.email
    user.first_name = updated_user.first_name
    user.last_name = updated_user.last_name
    user.hashed_password = hashed_password

    db.commit()
    db.refresh(user)
    return user
    
@router.delete("/{id}",
    response_model=list[schemas.ClinicUsersResponse],
    status_code=200,
    summary="Delete all the data of a speficied user",
    description="Delete name, last name, username, email and password of provided user using id.")
def delete_user(id: int, db: Session = Depends(get_db)):

    user = db.query(ClinicUsers).filter(ClinicUsers.id == id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return{"message":"user has been deleted successfully"}

    
    
    

