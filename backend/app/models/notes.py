from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Notes(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    clinic_user_id = Column(Integer, ForeignKey("clinic_users.id"), nullable=False)

    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    last_edited_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
