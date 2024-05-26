#import models
#from .user_condition import association_table
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import relationship
from models import BaseModel, Base


def User(BaseModel, Base):
    """
    User model
    """
    __tablename__ = 'users'
    name = Column(String(128), nullable=False)
    age = Column(Integer, nullable=True)
    weight = Column(Float, nullable=True)
    height = Column(Float, nullable=True)
    gender = Column(String(6), nullable=False)
    condition = relationship('Condition', secondary=association_table, back_populates='users')


    def __init__(self, gender):
        if gender == "male" or gender == "female":
            self.gender = gender
        else:
            self.gender = "male"

    @property
    def gender(self):
        """getter for gender"""
        return self.gender

    @property
    def blood_type(self):  
        """getter for blood types"""
        return self.blood_type

    @gender.setter
    def gender(self, value):
        """setter for gender"""
        if value == "male" or value == "female":
            self.gender = value

    def blood_type(self, value):
        """setter for blood types"""
        if value in ["O+", "O-", "A+", "A-", "B+", "B-", "AB", "AB-"]:
            self.blood_type = value
