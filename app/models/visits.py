#import models
from datetime import datetime
from sqlalchemy import Column, String, Float, Integer, ForeignKey,DateTime
from models.models import BaseModel, Base


class Visit(BaseModel, Base):
    """
    User model
    """
    __tablename__ = 'visits'
    condition_id = Column(String(60), ForeignKey('conditions.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.now())

