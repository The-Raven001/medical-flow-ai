from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas import notes as schemas
from app.models.notes import Notes
from app.models.patients import Patients

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.post("/",
    response_model=schemas.NotesResponse,
    status_code=200,
    summary="Create a new note",
    description="Creates a new note linked to the loaded patient."
    )
def create_note(note: schemas.NotesCreate, db: Session = Depends(get_db)):

    patient = db.query(Patients).filter(Patients.id == note.patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="patient not found")
    
    new_note = Notes(
        title=note.title,
        content=note.content,
        patient_id=note.patient_id,
        clinic_user_id=note.clinic_user_id
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@router.get("/",
    response_model=schemas.NotesResponse,
    status_code=200,
    summary="Retrieve all notes from all patients",
    description="Retrieve all notes from all patients with no distinction"
    )
def get_notes(db: Session = Depends(get_db)):
    notes = db.query(Notes).all()
    return notes

@router.get("/{id}",
    response_model=schemas.NotesResponse,
    status_code=200,
    summary="Retrieve specific note",
    description="Retrieve a specified note of a patient filtered by id"
    )
def get_note(id: int, db: Session = Depends(get_db)):

    note = db.query(Notes).fitler(Notes.id == id).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found.")
    return note

@router.put("/{id}",
    response_model=schemas.NotesResponse,
    status_code=200,
    summary="Edit selected note",
    description="Modify a selected note of patient filtered by id"
    )
def update_note(id: int, updated_note: schemas.NotesUpdate, db: Session = Depends(get_db)):

    note = db.query(Notes).filter(Notes.id == id).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    note.title = updated_note.title
    note.content = updated_note.content
    note.clinic_user_id = updated_note.clinic_user_id

    db.commit()
    db.refresh(note)
    return note

@router.delete("/{id}",
    response_model=dict,
    status_code=200,
    summary="Delete selected note",
    description="Erase selected note of a patient filtered by id."           
    )
def delete_note(id: int, db: Session = Depends(get_db)):

    note = db.query(Notes).filter(Notes.id == id).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    db.delete(note)
    db.commit()
    return {"message":"note has been deleted successfully"}
