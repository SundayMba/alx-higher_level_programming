#!/usr/bin/python3

"""
    model for state class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    """
        class model for state
    """
    __tablename__ = "states"
    id = Column(Integer,
                unique=True,
                autoincrement=True,
                nullable=False,
                primary_key=True
                )
    name = Column(String(128),
                  nullable=False,
                  unique=True
                  )
    cities = relationship("City", backref="state", cascade="all, delete")
