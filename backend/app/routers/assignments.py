from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.database import models
import jwt

router = APIRouter()

SECRET = "SECRET"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user(token: str, db: Session):
    payload = jwt.decode(token, SECRET, algorithms=["HS256"])
    user = db.query(models.User).get(payload["id"])
    return user

@router.post("/assignments")
def create_assignment(token: str, title: str, description: str, deadline: str, db: Session = Depends(get_db)):
    user = get_user(token, db)
    if user.role != "teacher":
        raise HTTPException(status_code=403, detail="Only teachers can create assignments")
    assignment = models.Assignment(title=title, description=description, deadline=deadline, created_by=user.id)
    db.add(assignment)
    db.commit()
    return {"message": "Assignment created"}

@router.get("/assignments")
def list_assignments(db: Session = Depends(get_db)):
    return db.query(models.Assignment).all()
