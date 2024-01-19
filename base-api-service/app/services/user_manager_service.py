from sqlalchemy.orm import Session
from app.models.user_db import User  # import your User model

class UserManager:
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, email: str):
        new_user = User(email=email)
        self.db.add(new_user)
        self.db.commit()
        return new_user

    def verify_user(self, email: str):
        user = self.get_user_by_email(email)
        if user:
            user.is_verified = True
            self.db.commit()
