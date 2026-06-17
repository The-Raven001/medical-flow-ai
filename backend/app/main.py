from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.clinic_users import router as clinic_users
from app.routes.intakes import router as intake
from app.routes.patients import router as patients  
from app.database import engine, Base
import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(clinic_users)
app.include_router(intake)
app.include_router(patients)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Backend running"}


