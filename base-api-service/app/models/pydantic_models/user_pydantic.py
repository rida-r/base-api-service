from pydantic import BaseModel, EmailStr
class VerificationRequest(BaseModel):
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class CodeVerification(BaseModel):
    email: EmailStr
    code: int
