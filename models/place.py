#!/usr/bin/python3
"""
Represents and defines the place class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place for a hbnb project.

    Attributes:
        city_id (str): The city id to which the place belongs.
        user_id (str): The user id of the place creator.
        name (str): The name of the place.
        description (str): Description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can
                         accommodate.
        price_by_night (int): The price per night for renting the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity.id's associated with the place.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
