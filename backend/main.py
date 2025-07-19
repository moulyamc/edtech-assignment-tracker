from fastapi import FastAPI
from app.routers import auth, assignments, submissions
from app.database import models
from app.database.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(assignments.router)
app.include_router(submissions.router)
