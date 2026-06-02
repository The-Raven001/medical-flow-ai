from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Patient(Base):
    __tablename__ = "patient"
    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    gender = Column(String, nullable=False)
    address = Column(String, nullable=False)
    preferred_language = Column(String)
    intake_status = Column(String, nullable=False, default="pending")
    emergency_contact_name = Column(String)
    emergency_contact_phone_number = Column(String)
    insurance_provider = Column(String, nullable=False)
    insurance_id = Column(String)


    email = Column(String, unique=True)
    provider_id = Column(
        Integer,
        ForeignKey("clinic_user.id"),
        nullable=False,
        unique=True
    )

    provider = relationship(
        "ClinicUser",
        back_populates="patients"
    )

    notes = relationship("Note", back_populates="patient", cascade="all, delete-orphan")
