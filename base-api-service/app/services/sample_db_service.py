from sqlalchemy.orm import Session
from app.models.sample_db import SampleDB
from app.models.pydantic_models.sample_db_pydantic import SampleDBUpdate, SampleDBResponse
from typing import List, Optional
from datetime import date

def create_db_entry(db: Session, entry_data: dict):
    new_entry = SampleDB(**entry_data)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

def delete_db_entry(db: Session , entry_id: int) -> bool:
    entry = db.query(SampleDB).filter(SampleDB.id == entry_id).first()
    if entry:
        db.delete(entry)
        db.commit()
        return True

    return False

def update_db_entry(db: Session, entry_id: int, updated_data: dict) -> SampleDBResponse:
    entry = db.query(SampleDB).filter(SampleDB.id == entry_id).first()
    if entry:
        update_data_dict = updated_data.dict(exclude_unset=True)
        for key, value in update_data_dict.items():
            if value is not None:
                setattr(entry, key, value)
        db.commit()
        db.refresh(entry)
        return entry
    return None

# def filter_db_entry():

# def find_entry_id():
def search_db_entries(db: Session, entry_id: Optional[int] = None, entry_date: Optional[date] = None) -> List[SampleDB]:
    query = db.query(SampleDB)
    if entry_id is not None:
        query = query.filter(SampleDB.id == entry_id)
    if entry_date is not None:
        query = query.filter(SampleDB.date == entry_date)
    return query.all()
