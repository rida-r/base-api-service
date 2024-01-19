from sqlalchemy.orm import Session
from app.models.user_db import User
from app.database import SessionLocal

# user manager service to deal with users in the db
class UserManager:

    def get_user_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def create_user(self, db: Session, email: str):
        new_user = User(email=email)
        db.add(new_user)
        db.commit()
        return new_user

    def verify_user(self, db: Session, email: str):
        user = self.get_user_by_email(db, email)
        if user:
            user.is_verified = True
            db.commit()
