from sqlalchemy import Column, Integer, Numeric, Date, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from app.database import Base
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    is_verified = Column(Boolean, default=False)
