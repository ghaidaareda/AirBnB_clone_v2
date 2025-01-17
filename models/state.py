#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete, delete-orphan", backref="state")
    else:
        @property
        def cities(self):
            """returns the list of City instances
            with state_id equals to the current State.id"""
            from models import storage
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
