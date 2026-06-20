from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.schemas import intakes as schemas
from app.models.intakes import Intakes
from app.models.patients import Patients

router = APIRouter(prefix="/intake", tags=["Intake"])

#Create intake notes

@router.post("/",
    response_model=schemas.IntakesResponse,
    status_code=200,
    summary="Create a new intake note",
    description="Create a new intake note from the patient that will be sent to the provider after being summarized by AI."       
    )
def create_intake(intake: schemas.IntakesCreate, db: Session = Depends(get_db)):
    
    patient = db.query(Patients).filter(Patients.id == intake.patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="patient not found.")

    new_intake = Intakes(
        title=intake.title,
        description=intake.description,
        patient_id=intake.patient_id
    )
    db.add(new_intake)
    db.commit()
    db.refresh(new_intake)
    return new_intake

#Retrieve intake notes

@router.get("/",
    response_model=schemas.IntakesResponse,
    status_code=200,
    summary="Retrieve intake notes",    
    description="Retrieve all intake notes from registered patients."
    )
def get_intakes(db: Session = Depends(get_db)):
    notes = db.query(Intakes).all()
    return notes


@router.get("/{id}",
    response_model=schemas.IntakesResponse,
    status_code=200,
    summary="Retrieve particular intake note",
    description="Retrieve a certain note filtered by note id."
    )
def get_intake(id: int, db: Session = Depends(get_db)):

    intake = db.query(Intakes).filter(Intakes.id == id).first()

    if not intake:
        raise HTTPException(status_code=404, detail="Intake note not found")
    return intake

#Update intake note

@router.put("/{id}",
    response_model=schemas.IntakesUpdate,
    status_code=200,
    summary="Edit selected intake note",
    description="Modify selected noted filtered by note id."
    )
def update_intake(id: int, updated_intake: schemas.IntakesUpdate, db: Session = Depends(get_db)):

    intake = db.query(Intakes).filter(Intakes.id == id).first()

    if not intake:
        raise HTTPException(status_code=404, detail="Intake note not found")
    
    intake.title = updated_intake.title
    intake.description = updated_intake.description

    db.commit()
    db.refresh(intake)
    return intake

#Delete intake note

@router.delete("/{id}",
    response_model=dict,
    status_code=200,
    summary="Delete selected intake note",
    description="Erase specified note of a patient, filtered by note id."
    )
def delete_intake(id: int, db: Session = Depends(get_db)):

    intake = db.query(Intakes).filter(Intakes.id == id).first()

    if not intake:
        raise HTTPException(status_code=404, detail="Intake note not found")
    
    db.delete(intake)
    db.commit()
    return {"message":"Intake note has been deleted successfully"}