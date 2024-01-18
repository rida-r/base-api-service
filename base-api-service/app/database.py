from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

DB_USER = os.getenv('POSTGRES_USER')  # Username
DB_PASS = os.getenv('POSTGRES_PASSWORD')  # Password
DB_HOST = os.getenv('POSTGRES_HOST')  # Hostname or IP
DB_PORT = os.getenv('POSTGRES_PORT', "5432")  # Port, default to 5432 if not set
DB_NAME = os.getenv('POSTGRES_DB')  # Database name


def create_database(dbname, user, password, host, port=5432):
    # open a connection to the default postgres database
    conn = psycopg2.connect(dbname='postgres', user=user, password=password, host=host, port=port)
    # set isolation level of connection because certain commands cannot be run inside of a transaction block
    # makes sure sql commands are immediately committed to db
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # check if the db already exists before creating the db
    with conn.cursor() as cursor:
        # pg_catalog.pg_database - system catalog table in pgsql that contains information about databases
        # %s represents a parameter, in this case, dbname
        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (dbname,))
        exists = cursor.fetchone()
        if not exists:
            cursor.execute("CREATE DATABASE " + psycopg2.sql.Identifier(dbname).as_string(conn))

    # close connection to psql server
    conn.close()


create_database(DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT)

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def init_db():
    from .models.sample_db import SampleDB
    Base.metadata.create_all(bind=engine)