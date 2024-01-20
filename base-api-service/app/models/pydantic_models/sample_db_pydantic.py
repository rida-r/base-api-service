
from pydantic import BaseModel
from datetime import date
from typing import Optional

class SampleDBCreate(BaseModel):
    date: date
    current_assets: float
    non_current_assets: float
    current_liabilities: float
    non_current_liabilities: float
    shareholders_equity: float

class SampleDBResponse(BaseModel):
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

class SampleDBUpdate(BaseModel):
    date: Optional[date] = None
    current_assets: Optional[float] = None
    non_current_assets: Optional[float] = None
    current_liabilities: Optional[float] = None
    non_current_liabilities: Optional[float] = None
    shareholders_equity: Optional[float] = None
