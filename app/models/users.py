
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import relationship
from models.models import BaseModel, Base


class User(BaseModel, Base):
    """
    User model
    """
    __tablename__ = 'users'
    name = Column(String(128), nullable=False)
    age = Column(Integer, nullable=True)
    weight = Column(Float, nullable=True)
    height = Column(Float, nullable=True)
    gender = Column(String(10), nullable=False)
    blood_type = Column(String(3), nullable=True)

    @property
    def blood_type(self):
        """getter for blood types"""
        return self._blood_type

    @blood_type.setter
    def blood_type(self, value):
        """setter for blood types"""
        if value in ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]:
            self._blood_type = value
        else:
            self._blood_type = None