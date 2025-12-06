from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FeedbackBase(BaseModel):
    username: str
    rating: int
    comment: Optional[str]=None

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackResponse(FeedbackBase):
    id: int
    status: str
    created_at: datetime

    class config:
        orm_mode=True