#!/usr/bin/python3

"""
    module that models city object
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, ForeignKey

Base = declarative_base()

class City(Base):
    """
        class that models city
        id: sqlalchemy.integer, primary key, autoincrement, not null
        name: sqlalchemy.String, String(128), not null
        state_id: foreign_key, not null, Integer
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
