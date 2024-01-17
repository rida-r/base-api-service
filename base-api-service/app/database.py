from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

DB_USER = os.getenv('POSTGRES_USER')  # Username
DB_PASS = os.getenv('POSTGRES_PASSWORD')  # Password
DB_HOST = os.getenv('POSTGRES_HOST')  # Hostname or IP
DB_PORT = os.getenv('POSTGRES_PORT', "5432")  # Port, default to 5432 if not set
DB_NAME = os.getenv('POSTGRES_DB')  # Database name

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def init_db():
    from .models.balance_sheet import BalanceSheet
    Base.metadata.create_all(bind=engine)