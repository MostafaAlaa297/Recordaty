import models
from datetime import datetime
from sqlalchemy import Column, String, Float, Integer, ForeignKey,DateTime
from models import BaseModel, Base


def Visit(BaseModel, Base):
    """
    User model
    """
    __tablename__ = 'visits'
    condition_id = Column(String(60), ForeignKey('condition.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.now())

