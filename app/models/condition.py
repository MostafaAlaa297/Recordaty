from models.models import BaseModel, Base
import sqlalchemy
#from .user_condition import association_table
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

class Condition(BaseModel, Base):
    """
    condition model
    """
    __tablename__ = 'conditions'
    condition_name = Column(String(128), nullable=False)

    visits = relationship("Visit", backref="conditions", cascade="all, delete")
    reports = relationship("Report", backref="conditions", cascade="all, delete")

    user_condition = Table('user_condition', Base.metadata,
                          Column('user_id', String(60),
                                ForeignKey('users.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                                primary_key=True),
                          Column('condition_id', String(60),
                                 ForeignKey('conditions.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))
