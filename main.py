from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from database import localsession, engine
import models
from schemas import FeedbackCreate, FeedbackResponse

api=FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db=localsession()
    try:
        yield db
    finally:
        db.close()

# Basic index route
@api.get("/")
def index():
    return {"Message":"Hi this a CRUD application using fastAPI!"}



# Adding a feedback - POST
@api.post(
    "/feedbacks",
    response_model=FeedbackResponse,
    status_code=status.HTTP_201_CREATED
)
def create_feedback(feedback: FeedbackCreate, db:Session= Depends(get_db)):
    status_rating= "Positive" if feedback.rating>=6 else "Negative"

    db_feedback=models.Feedback(
        username=feedback.username,
        rating=feedback.rating,
        comment=feedback.comment,
        status=status_rating,
        created_at=datetime.utcnow()
    )

    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)   #id will be created here

    return db_feedback



# Getting all the feedbacks - GET
@api.get(
    "/feedbacks",
    response_model=List[FeedbackResponse]
)
def get_feedbacks(db:Session= Depends(get_db)):
    feedbacks=db.query(models.Feedback).all()
    return feedbacks



# Getting one feedback - GET
@api.get(
    "/feedbacks/{id}",
    response_model=FeedbackResponse
)
def get_one(id: int, db:Session= Depends(get_db)):
    fb=db.query(models.Feedback).filter(models.Feedback.id==id).first()
    if fb is None:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return fb



# Update a feedback - PUT
@api.put(
    "/feedbacks/{id}",
    response_model=FeedbackResponse
)
def update_feedbacks(id: int, updated: FeedbackCreate, db:Session= Depends(get_db)):

    fb = db.query(models.Feedback).filter(models.Feedback.id==id).first()
    if fb is None:
        raise HTTPException(status_code=404, detail="Cannot update, feedback not found")

    fb.username=updated.username
    fb.rating=updated.rating
    fb.comment=updated.comment
    fb.status= "Positive" if updated.rating>=6 else "Negative"

    db.commit()
    db.refresh(fb)
    return fb



# Deleting a feedback - DELETE
@api.delete("/feedbacks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def del_feedback(id: int, db:Session= Depends(get_db)):

    fb = db.query(models.Feedback).filter(models.Feedback.id==id).first()
    if fb is None:
        raise HTTPException(status_code=404, detail="Cannot delete, feedback not found")

    db.delete(fb)
    db.commit()
    return
