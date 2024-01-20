from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from app.services.sample_db_service import create_db_entry, delete_db_entry, update_db_entry
from app.database import SessionLocal
from app.models.pydantic_models.sample_db_pydantic import SampleDBCreate, SampleDBResponse, SampleDBUpdate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sample-db/", response_model=SampleDBResponse)
def add_entry_endpoint(entry: SampleDBCreate, db: Session = Depends(get_db)):
    try:
        entry_data = entry.model_dump()
        return create_db_entry(db, entry_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/delete-entry/{entry_id}")
def delete_entry_endpoint(entry_id: int, db: Session = Depends(get_db)):
    if delete_db_entry(db, entry_id):
        return {"message" : "Entry deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Entry not found")

@router.put("/update-entry/{entry_id}", response_model=SampleDBResponse)
def update_entry_endpoint(entry_id: int, updated_data: SampleDBUpdate = Body(...), db: Session = Depends(get_db)):
    updated_entry = update_db_entry(db, entry_id, updated_data)
    if updated_entry:
        return updated_entry
    else:
        raise HTTPException(status_code=404, detail="Entry not found")