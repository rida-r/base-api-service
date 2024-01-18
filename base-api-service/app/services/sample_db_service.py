from sqlalchemy.orm import Session
from app.models.sample_db import SampleDB

def create_db_entry(db: Session, entry_data: dict):
    new_entry = SampleDB(**entry_data)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry
