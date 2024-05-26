from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
#import models


association_table = Table('association', models.models.Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('condition_id', Integer, ForeignKey('condition.id'))
)
