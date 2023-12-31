#!/usr/bin/python3
"""
The Filestorage class handling both serialization and deserialization
"""
from encodings import utf_8
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to
    instances."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {obj_id: obj.to_dict()
                    for obj_id, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf_8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects if file exists, otherwise
        do nothing."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf_8') as f:
                objs = json.load(f)
                for obj_id, obj_data in objs.items():
                    cls_name = obj_data['__class__']
                    cls = globals()[cls_name]
                    self.new(cls(**obj_data))
        except FileNotFoundError:
            pass
