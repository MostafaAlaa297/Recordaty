import models
from .user_condition import association_table
from sqlalchemy import Column, String, Float, Integer, relationship

def User(Model, Base):
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
      return self.gender

    @gender.setter
    def gender(self, value):
        if value == "male" or value == "female":
            self.gender = value
