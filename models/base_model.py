#!/usr/bin/python3
"""
Module to define all models
"""

import uuid
from sqlalchemy import MetaData

Base = MetaData()

class Base_model:
    """Class that defines a user"""

    def __init__(self):
        self.id = uuid.uuid4()