import models
from models import BaseModel, Base
from datetime import datetime
from sqlalchemy import Column, String, Float, Integer, ForeignKey,DateTime
def Report(BaseModel, Base):
    """
    Report model
    """
    __tablename__ = 'reports'
    condition_id = Column(String(60), ForeignKey('condition.id'), nullable=False)
    Report_date = Column(DateTime, default=datetime.now())
