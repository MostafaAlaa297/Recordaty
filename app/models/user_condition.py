from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

association_table = Table('association', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('condition_id', Integer, ForeignKey('condition.id'))
)