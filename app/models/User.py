from models import BaseEntity
from sqlalchemy import Column
from sqlalchemy.types import DateTime, String

class User(BaseEntity):
    username: String = Column(String, primary_key=True)
    email: String = Column(String)
    password: String = Column(String)
    birth_date: DateTime = Column(DateTime) 

