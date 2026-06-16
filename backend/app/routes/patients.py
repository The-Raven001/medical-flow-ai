from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db 
from sqlalchemy.orm import Session
from app.schemas import patients as schemas
from app.models.patients import Patients

router = APIRouter(prefix="/patients", tags=["Patients"])

#Create patient profile

@router.post("/",
    response_model=schemas.PatientsBase,
    status_code=201,
    summary="Create a new patient profile",
    description="Create a new profile for a patient taking their demographics and relevant information in order to be stored in the database."
    )
def create_patient(patient: schemas.PatientsBase, db: Session = Depends(get_db)):

    new_patient = Patients(
        first_name=patient.first_name,
        last_name=patient.last_name,
        date_of_birth=patient.date_of_birth,
        phone_number=patient.phone_number,
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
    response_model=schemas.PatientsSummary,
    status_code=200,
    summary="Retrieve shallow data from patients",
    description="Retrieve all patients based on common identifiers." 
    )
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patients).all()

@router.get("/{id}",
    response_model=schemas.PatientsBase,
    status_code=201,
    summary="Retrieve all data from one patient.",
    description=""
    )
def get_patient(id: int, db: Session = Depends(get_db)):

    patient = db.query(Patients).filter(Patients.id == id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="patient not found")
    return patient

#Update patient

@router.put("/{id}",
    response_model=schemas.PatientsBase,
    status_code=200,
    summary="Update data of a given patient",
    description="Modify given data of a patient filtered by the id of the patient stored in the database."
    )
def update_patient(id: int, updated_patient:schemas.PatientBase, db: Session = Depends(get_db)):

    patient = db.query(Patients).filter(Patients.id == id).first()

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
    response_model=schemas.PatientsBase,
    status_code=200,
    summary="Delete all the data of a given patient",
    description="Erase all data from the referred patient, patient is filtered based on the id related to him in the database."
    )
def delete_patient(id: int, db: Session = Depends(get_db)):

    patient = db.query(Patients).filter(Patients.id == id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="patient not found")
    db.delete(patient)
    db.commit()
    return {"message":"Patient profile deleted successfully"}
