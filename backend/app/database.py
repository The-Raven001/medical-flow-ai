from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflus=False, bind=engine)
Base = declarative_base()

def get_deb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()