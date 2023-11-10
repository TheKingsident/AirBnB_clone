#!/usr/bin/python3
"""
Defines and represents the city class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city for a hbnb project.

    Attributes:
        state_id (str): The state id to which the city belongs.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
