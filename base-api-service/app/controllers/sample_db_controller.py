from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.sample_db_service import create_db_entry
from app.database import SessionLocal
from app.models.pydantic_models.sample_db_pydantic import SampleDBCreate, SampleDBResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sample-db/", response_model=SampleDBResponse)
def add_db_entry(entry: SampleDBCreate, db: Session = Depends(get_db)):
    try:
        entry_data = entry.model_dump()
        return create_db_entry(db, entry_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
