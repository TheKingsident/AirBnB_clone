"""
Initialization of the Model package.

This module initializes the package by setting up a FileStorage instance and
reloading any existing data from the JSON file storage.
"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
