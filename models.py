from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Feedback(Base):
    __tablename__='feedbacks'

    id=Column(Integer, primary_key=True, index=True)
    username=Column(String, nullable=False)
    rating=Column(Integer, nullable=False)
    comment=Column(String, nullable=False)
    status=Column(Integer, nullable=False)
    created_at=Column(DateTime, default=datetime.utcnow)