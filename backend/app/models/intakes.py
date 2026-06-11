from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func 
from app.database import Base

class Intakes(Base):
    __tablename__ = "intakes"
    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    last_edited = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    patient = relationship("Patients", back_populates="intakes")