#!/usr/bin/python3
"""City """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class City(Base):
    """City class"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),
                      autoincrement=True, nullable=False)
