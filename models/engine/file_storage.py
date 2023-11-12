#!/usr/bin/python3
"""
The Filestorage class handling both serialization and deserialization
"""
from encodings import utf_8
import json
from models.base_model import BaseModel
from models.user import User


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
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf_8') as f:
                objs = json.load(f)
                for obj_id, obj_data in objs.items():
                    cls_name = obj_data['__class__']
                    cls = globals().get(cls_name)
                    if cls:  # Ensure that cls is not None
                        try:
                            self.new(cls(**obj_data))
                        except TypeError as e:
                            print(f"TypeError when attempting to create {cls_name} with data {obj_data}: {e}")
                        except Exception as e:
                            print(f"Unexpected error when creating {cls_name}: {e}")
                    else:
                        print(f"Class {cls_name} not found in global scope.")
        except FileNotFoundError:
            print("JSON file not found.")
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        """
