from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.clinic_users import router as clinic_users
from app.database import engine, Base
import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(clinic_users)

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


