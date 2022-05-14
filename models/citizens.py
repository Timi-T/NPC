#!/usr/bin/python3
"""
Module to define a Citizen
"""

from base_model import Base_model, Base
from sqlalchemy import String, Column, Integer

class Citizen(Base_model, Base):
    """Class that defines a Citizen"""

    __tablename__ = 'Citizens'
    id = Column(String(64), nullable=False)
    name = Column(String(64), nullable=False)
    gender = Column(String(32), nullable=False)
    address = Column(String(64), nullable=False)
    phone = Column(Integer)
    ward_id = Column(String(64), ForeignKey=True, nullable=False)

    def __init__(self, name, gender, address, phone, ward_id):
        super().__init__()
        self.name = name
        self.gender = gender
        self.address = address
        self.phone = phone
        self.state_id = ward_id

