from sqlalchemy.orm import Session
from app.models.balance_sheet import BalanceSheet

def create_balance_sheet_entry(db: Session, entry_data: dict):
    new_entry = BalanceSheet(**entry_data)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry
