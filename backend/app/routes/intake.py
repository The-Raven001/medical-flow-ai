from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas import intake as schemas
from backend.app.models import intake as models

router = APIRouter(prefix="/intake", tags=["Intake"])

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
