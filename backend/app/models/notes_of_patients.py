from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Note(Base):
    __tablename__ = "notes_of_patients"
    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False())
    last_edited = Column(DateTime(timezone=True), server_default=func.now(), nullable=False())
    last_edited_by = Column(String, nullable=False)

    patient = relationship("PatientUser")