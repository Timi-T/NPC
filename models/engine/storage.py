#!/usr/bin/python3
"""
Module to handle storage of objects to the database
"""

from unicodedata import name
from models.base_model import Base
from models.users import User
from models.states import State
from models.lga import LGA
from models.wards import Ward
from models.citizens import Citizen
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

all_classes = {"User": User, "State": State, "LGA": LGA, "Ward": Ward, "Citizen": Citizen}

class DB_storage():
    """Database storage class"""

    __session = None
    __engine = None

    def __init__(self):
        """Initialize a database"""
        user = os.getenv("NPC_USER")
        host = os.getenv("NPC_HOST")
        db = os.getenv("NPC_DB")
        pwd = os.getenv("NPC_PASSWORD")
        txt = "mysqldb+mysql://{}:{}@{}/{}".format(user, pwd, host, db)
        self.__engine = create_engine(txt, pool_pre_ping=True)

    def reload(self):
        """Reload the database for updates"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session


    def new(self, obj):
        """Add a new object to the database session"""

        self.__session.add(obj)
    
    def save(self):
        """Save all added objects to the database"""

        self.__session.save()

    def get(self, cls_name, obj_id):
        """Get an object given the object name and the object id"""

        for k, v in all_classes.items():
            if k == cls_name:
                all_objs = self.__session.query(v).all()
                for obj in all_objs:
                    if obj.id == obj_id:
                        return obj
                return "Object doesnt exist"
            return "Class doesn't exist"

    def all(self, cls):
        """Function to get all objects in a class"""

        for k, v in all_classes.items():
            if k == cls:
                all_objs = self.__session.query(v).all()
                return all_objs
            return "Class doesn't exist"
        