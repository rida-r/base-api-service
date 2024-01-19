from jose import jwt, JWTError
from datetime import datetime, timedelta
import random
import os

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_secret_key")
ALGORITHM = "HS256"
def send_verification_email(email: str, code: int):
    # add email sending stuff
    pass

def generate_verification_code() -> int:
    return random.randint(100000, 999999)

def create_access_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
