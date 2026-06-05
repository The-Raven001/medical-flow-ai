from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db 
from sqlalchemy.orm import Session
from app.schemas import patients as schemas
from app.models import patients as models

router = APIRouter(prefix="/patients", tags=["Patients"])

#Create patient profile

@router.post("/",
    response_model=schemas.PatientBase,
    status_code=201,
    summary="Create a new patient profile",
    description=""
    )
def create_patient(patient: schemas.PatientBase, db: Session = Depends(get_db)):

    new_patient = models.Patient(
        first_name=patient.first_name,
        last_name=patient.last_name,
        date_of_birth=patient.date_of_birth,
        gender=patient.gender,
        address=patient.address,
        preferred_language=patient.preferred_language,
        intake_status=patient.intake_status,
        emergency_contact_name=patient.emergency_contact_name,
        emergency_contact_phone_number=patient.emergency_contact_phone_number,
        insurance_provider=patient.insurance_provider,
        insurance_id=patient.insurance_id,
        email=patient.email,
        prorvider_id=patient.provider_id

    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

#Get all patient or individually.

@router.get("/",
    response_model=schemas.PatientSummary,
    status_code=200,
    summary="Retrieve shallow data from patients",
    description="" 
    )
def get_patients(db: Session = Depends(get_db)):
    return db.query(models.Patient).all()

@router.get("/{id}",
    response_model=schemas.PatientBase,
    status_code=201,
    summary="Retrieve all data from one patient.",
    description=""
    )
def get_patient(id: int, db: Session = Depends(get_db)):

    patient = db.query(models.Patient).filter(models.Patient.id == id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="patient not found")
    return patient

#Update patient

@router.put("/{id}",
    response_model=schemas.PatientBase,
    status_code=200,
    summary="Update data of a given patient",
    description=""
    )
def update_patient(id: int, updated_patient:schemas.PatientBase, db: Session = Depends(get_db)):

    patient = db.query(models.Patient).filter(models.Patient.id == id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="patient not found")
    
#You might want to add if statements here to check if the email or username exists in the database
#already as it might throw an error given that those two are unique.
    
    patient.first_name = updated_patient.first_name
    patient.last_name = updated_patient.last_name
    patient.email = updated_patient.email
    patient.date_of_birth = updated_patient.date_of_birth
    patient.gender = updated_patient.gender
    patient.preferred_language = updated_patient.preferred_language
    patient.intake_status = updated_patient.intake_status
    patient.emergency_contact_name = updated_patient.emergency_contact_name
    patient.emergency_contact_phone_number = updated_patient.emergency_contact_phone_number
    patient.insurance_provider = updated_patient.insurance_provider
    patient.insurance_id = updated_patient.insurance_id

    db.commit()
    db.refresh(patient)
    return patient

@router.delete("/{id}",
    response_model=schemas.PatientBase,
    status_code=200,
    summary="Delete all the data of a given patient",
    description=""
    )
def delete_patient(id: int, db: Session = Depends(get_db)):

    patient = db.query(models.Patient).filter(models.Patient.id == id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="patient not found")
    db.delete(patient)
    db.commit()
