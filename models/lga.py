#!/usr/bin/python3
"""
Module to define a LGA
"""

from base_model import Base_model, Base
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class LGA(Base_model, Base):
    """Class that defines a Local government"""

    __tablename__ = 'LGAs'
    id = Column(String(64), nullable=False)
    name = Column(String(64), nullable=False)
    state_id = Column(String(64), ForeignKey("States.id"), nullable=False)
    lgas = relationship("LGA", backref="States", cascade="all, delete, delete-orphan")


    def __init__(self, name, state_id):
        super().__init__()
        self.name = name
        self.state_id = state_id