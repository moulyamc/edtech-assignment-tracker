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

@router.post("/assignments/{assignment_id}/submit")
def submit_assignment(assignment_id: int, token: str, content: str, db: Session = Depends(get_db)):
    user = get_user(token, db)
    if user.role != "student":
        raise HTTPException(status_code=403, detail="Only students can submit assignments")
    submission = models.Submission(assignment_id=assignment_id, student_id=user.id, content=content)
    db.add(submission)
    db.commit()
    return {"message": "Submission successful"}

@router.get("/assignments/{assignment_id}/submissions")
def view_submissions(assignment_id: int, token: str, db: Session = Depends(get_db)):
    user = get_user(token, db)
    if user.role != "teacher":
        raise HTTPException(status_code=403, detail="Only teachers can view submissions")
    return db.query(models.Submission).filter(models.Submission.assignment_id == assignment_id).all()
