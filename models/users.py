#!/usr/bin/python3
"""
Module to define a user
"""

from base_model import Base_model, Base
from sqlalchemy import String, Column, Integer
from flask_login import UserMixin
from api.v1.app import loginmanager

@loginmanager.user_loader
def get_user(user_id):
    """Retrieve a user for login"""
    from models import storage

    user = storage.get("User", user_id)
    return user

class User(Base_model, Base, UserMixin):
    """Class that defines a user"""

    __tablename__ = 'Users'
    id = Column(String(64), nullable=False)
    name = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)

    def __init__(self, name, email, password):
        super().__init__()
        self.name = name
        self.email = email
        self.password = password