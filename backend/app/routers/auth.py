from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.database import models
from passlib.hash import bcrypt
import jwt

router = APIRouter()

SECRET = "SECRET"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(name: str, email: str, password: str, role: str, db: Session = Depends(get_db)):
    hashed = bcrypt.hash(password)
    user = models.User(name=name, email=email, password=hashed, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created"}

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user or not bcrypt.verify(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = jwt.encode({"id": user.id, "role": user.role}, SECRET, algorithm="HS256")
    return {"token": token}
