from fastapi import APIRouter, Depends, HTTPException, status
from app.models.pydantic_models.user_pydantic import VerificationRequest, Token, CodeVerification
from app.services.user_service import send_verification_email, generate_verification_code, create_access_token
import os
from datetime import timedelta
from app.services.user_manager_service import UserManager
from app.database import SessionLocal


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
verification_codes = {}

user_manager = UserManager(SessionLocal)
@router.post("/request-verification/")
async def request_verification(request: VerificationRequest):
    code = generate_verification_code()
    verification_codes[request.email] = code
    send_verification_email(request.email, code)
    return {"message": "Verification code sent to your email"}

@router.post("/verify-code/", response_model=Token)
async def verify_code(verification: CodeVerification):
    if verification.email in verification_codes:
        if verification_codes[verification.email] == verification.code:
            user_manager.verify_user(verification.email)

            access_token = create_access_token(
                data={"sub": verification.email},
                expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            )

            return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid verification code")
