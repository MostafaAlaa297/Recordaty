#import models
#from models.user_condition import association_table
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.condition import Condition
from models.models import BaseModel
from models.reports import Report
from models.users import User
from models.visits import Visit

classes = {"Visit": Visit, "Report": Report,
           "Condition": Condition, "User": User}

class Database:
    """
    Database configurations
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        create engine
        """
        self.__engine = create_engine('mysql+mysqldb://Recordaty:recordaty_ALX!@localhost/recordaty')

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()
