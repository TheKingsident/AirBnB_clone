#!/usr/bin/python3
"""
Represents and defines the review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review for a hbnb project.

    Attributes:
        place_id (str): The place id to which the review belongs.
        user_id (str): The user id of the reviewer.
        text (str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
