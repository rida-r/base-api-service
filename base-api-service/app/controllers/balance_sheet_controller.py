# controllers/balance_sheet_controller.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.balance_sheet_service import create_balance_sheet_entry
from app.database import SessionLocal
from app.models.pydantic_models.balance_sheet_pydantic import BalanceSheetCreate, BalanceSheetResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/balance-sheet/", response_model=BalanceSheetResponse)
def add_balance_sheet_entry(entry: BalanceSheetCreate, db: Session = Depends(get_db)):
    try:
        entry_data = entry.model_dump()
        return create_balance_sheet_entry(db, entry_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
