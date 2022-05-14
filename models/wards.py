#!/usr/bin/python3
"""
Module to define a Ward
"""

from base_model import Base_model
from sqlalchemy import String, Column, Integer, ForeignKey

from models.base_model import Base

class Ward(Base_model, Base):
    """Class that defines a Local government Ward"""

    __tablename__ = 'Wards'
    id = Column(String(64), nullable=False)
    name = Column(String(64), nullable=False)
    lga_id = Column(String(64), ForeignKey("LGAs.id"), nullable=False)


    def __init__(self, name, lga_id):
        super().__init__()
        self.name = name
        self.state_id = lga_id