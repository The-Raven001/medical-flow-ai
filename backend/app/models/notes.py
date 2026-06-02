from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func 
from app.database import Base

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    last_edited = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    last_edited_by_id = Column(Integer, ForeignKey("clinic_user.id"))

    patient_id = Column(Integer, ForeignKey("patietns.id"), nullable=False)
    patient = relationship("PatientUser", back_populates="notes")