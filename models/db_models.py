from db.base import Base
from sqlalchemy import Boolean, Column, Integer, String, Float
from sqlalchemy.types import DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from random import randint

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String,index=True, unique=True)
    hashed_pword = Column(String)

class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String, index=True, unique=False, nullable=False)
    item_name = Column(String, index=True, unique=False, nullable=False)
    item_price = Column(String, index=True, unique=False, nullable=False)
    