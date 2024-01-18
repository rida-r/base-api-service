from sqlalchemy import Column, Integer, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base
from app.database import Base

class SampleDB(Base):
    __tablename__ = 'sample_db'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    current_assets = Column(Numeric(10, 2), nullable=False)
    non_current_assets = Column(Numeric(10, 2), nullable=False)
    current_liabilities = Column(Numeric(10, 2), nullable=False)
    non_current_liabilities = Column(Numeric(10, 2), nullable=False)
    shareholders_equity = Column(Numeric(10, 2), nullable=False)

    @property
    def total_assets(self):
        return self.current_assets + self.non_current_assets

    @property
    def total_liabilities_and_equity(self):
        return self.current_liabilities + self.non_current_liabilities + self.shareholders_equity
