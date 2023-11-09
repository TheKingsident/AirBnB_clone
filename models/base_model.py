#!/usr/bin/python3
"""
A module that defines a Base class
Subsequent classes ma inherit from this
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class that defines all common attributes and methods for other
    classes.

    Attributes:
        id (str): Unique id assigned with an uuid when an instance is created.
        created_at (datetime): Assigned with the current datetime when an
        instance is created.
        updated_at (datetime): Assigned with the current datetime when an
                            instance is created
                               and updated every time the object is modified.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel, assigning id, created_at
        and updated_at.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Defines the string representation of the BaseModel instance.

        Returns:
            str: A string representation of the BaseModel instance,
                 including the class name, id, and dictionary of all
                 the instance attributes.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Creates a dictionary containing all keys/values of the instance's
        __dict__.

        The returned dictionary includes an additional key '__class__' with
        the name of the class and ensures 'created_at' and 'updated_at'
        are represented as strings in ISO format.

        Returns:
            dict: A dictionary containing all keys/values of the instance's
                  __dict__.
        """
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
