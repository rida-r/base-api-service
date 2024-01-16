from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()  # This loads the environment variables from a .env file

# Now you can use os.getenv to read environment variables
db_user = os.getenv("DATABASE_USER")
db_password = os.getenv("DATABASE_PASSWORD")
print(db_user)

app = FastAPI()
