import models
import sqlalchemy
from .user_condition import association_table
from sqlalchemy import Column, String, relationship
from models import BaseModel, Base


def Condition(BaseModel, Base):
    """
    condition model
    """
    __tablename__ = 'conditions'
    condition_name = Column(String(128), nullable=False)

    users = relationship('User', secondary=association_table, back_populates='conditions')
    visits = relationship("Visit", backref="condition", cascade="all, delete")
    reports = relationship("Report", backref="condition", cascade="all, delete")

