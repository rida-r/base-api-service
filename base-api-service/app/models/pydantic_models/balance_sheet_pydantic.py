
from pydantic import BaseModel
from datetime import date

class BalanceSheetCreate(BaseModel):
    date: str
    current_assets: float
    non_current_assets: float
    current_liabilities: float
    non_current_liabilities: float
    shareholders_equity: float

class BalanceSheetResponse(BaseModel):
    id: int
    date: date
    current_assets: float
    non_current_assets: float
    current_liabilities: float
    non_current_liabilities: float
    shareholders_equity: float

    class Config:
        orm_mode = True
        json_encoders = {
            date: lambda v: v.strftime("%Y-%m-%d"),
        }
