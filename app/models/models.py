import sqlalchemy
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class BaseModel:
    """
    Base Model
    """
    id = Column(String(60), primary_key=True)
    
    def __init__(self, *args, **kwargs):    
        """
        setting up id
        """
        self.id = str(uuid.uuid4())

    def save(self):
        """ save the object """
        models.storage.new(self)
        models.storage.save()
    
    def delete(self):
        """ delet the object """
        models.storage.delete(self)


