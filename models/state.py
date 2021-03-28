#!/usr/bin/python3
""" State Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):

    """ State class """
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete', backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """File storage getter"""
            citylist = []
            for obj in models.hbnb_storage.all():
                if obj.state_id == self.id:
                    citylist.append(obj)
            return citylist
