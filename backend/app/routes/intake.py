from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas import intake as schemas
from backend.app.models import intake as models

router = APIRouter(prefix="/intake", tags=["Intake"])

#Create intake notes

@router.post("/",
    response_model=schemas.Intake,
    status_code=200,
    summary="Create a new intake note",
    description=""       
    )
def create_intake(intake: schemas.Intake, db: Session = Depends(get_db)):
    
    new_intake = models.Intake(
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
    response_model=schemas.Intake,
    status_code=200,
    summary="Retrieve intake notes",    
    description=""
    )
def get_intakes(db: Session = Depends(get_db)):
    notes = db.query(models.Intake).all()
    return notes


@router.get("/{id}",
    response_model=schemas.Intake,
    status_code=200,
    summary="Retrieve particular intake note",
    description=""
    )
def get_intake(id: int, db: Session = Depends(get_db)):

    intake = db.query(models.Intake).filter(models.Intake.id == id).first()

    if not intake:
        raise HTTPException(status_code=404, detail="Intake note not found")
    return intake

#Update intake note

@router.put("/{id}",
    response_model=schemas.Intake,
    status_code=200,
    summary="Edit selected intake note",
    description=""
    )
def update_intake(id: int, updated_intake: schemas.IntakeUpdate, db: Session = Depends(get_db)):

    intake = db.query(models.Intake).filter(models.Intake.id == id).first()

    if not intake:
        raise HTTPException(status_code=404, detail="Intake note not found")
    
    intake.title = updated_intake.title
    intake.description = updated_intake.description
    intake.patient_id = updated_intake.patient_id

    db.commit()
    db.refresh(intake)
    return intake

#Delete intake note

@router.delete("/{id}",
    response_model=schemas.Intake,
    status_code=200,
    summary="Delete selected intake note",
    description=""
    )
def delete_intake(id: int, db: Session = Depends(get_db)):

    intake = db.query(models.Intake).filter(models.Intake.id == id).first()

    if not intake:
        raise HTTPException(status_code=404, detail="Intake note not found")
    
    db.delete(intake)
    db.commit()
    return {"message":"Intake note has been deleted successfully"}