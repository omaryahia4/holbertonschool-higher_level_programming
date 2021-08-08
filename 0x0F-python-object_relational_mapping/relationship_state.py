#!/usr/bin/python3
"""Module state"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(256), nullable=False)
    cities = relationship("City", backref="state")
