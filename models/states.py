#!/usr/bin/python3
"""
Module to define a state
"""

from base_model import Base_model, Base
import sqlalchemy
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship

class State(Base_model, Base):
    """Class that defines state"""

    __tablename__ = 'States'
    id = Column(String(64), nullable=False)
    name = Column(String(64), nullable=False)
    lgas = relationship("State", backref="LGAs", cascade="all, delete, delete-orphan")

    def __init__(self, name):
        super().__init__()
        self.name = name