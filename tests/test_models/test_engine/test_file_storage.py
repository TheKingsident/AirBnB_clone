#!/usr/bin/python3
"""
This module is a unittest for the FileStorage class
"""
import tempfile
import shutil
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        FileStorage._FileStorage__file_path = os.path.join(
            self.temp_dir, 'temp_file.json')
        self.storage = FileStorage()

    def tearDown(self):
        # Remove the temporary directory after the test
        shutil.rmtree(self.temp_dir)

    def test_all_method(self):
        """Test the all method of FileStorage."""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict,
                              "all should return a dictionary")

    def test_new_method(self):
        """Test the new method of FileStorage."""
        storage = FileStorage()
        instance = BaseModel()
        storage.new(instance)
        all_objects = storage.all()
        key = f"{instance.__class__.__name__}.{instance.id}"
        self.assertIn(key, all_objects, "New object should be in storage")

    def test_save_method(self):
        """Test the save method of FileStorage."""
        instance = BaseModel()
        self.storage.new(instance)
        self.storage.save()
        with open(FileStorage._FileStorage__file_path, 'r') as file:
            data = file.read()
            self.assertIn(instance.id, data, "New object's id in saved file")

    def test_reload_method(self):
        """Test the reload method of FileStorage."""
        storage = FileStorage()
        instance = BaseModel()
        storage.new(instance)
        storage.save()
        storage.reload()
        all_objects = storage.all()
        key = f"{instance.__class__.__name__}.{instance.id}"
        self.assertIn(key, all_objects, "Saved object in reloaded storage")

    def test_file_creation(self):
        """Test file creation on save."""
        self.storage.new(BaseModel())
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path),
                        "File created on save")

    def test_save_with_multiple_objects(self):
        """Test saving multiple objects."""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.storage.new(instance1)
        self.storage.new(instance2)
        self.storage.save()

        with open(FileStorage._FileStorage__file_path, 'r') as f:
            content = f.read()
            self.assertIn(instance1.id, content, "First object's id in file")
            self.assertIn(instance2.id, content, "Second object's id in file")

    def test_reload_with_multiple_objects(self):
        """Test reloading multiple objects."""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.storage.new(instance1)
        self.storage.new(instance2)
        self.storage.save()

        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn(f"{instance1.__class__.__name__}.{instance1.id}",
                      all_objects, "First object in reloaded storage")
        self.assertIn(f"{instance2.__class__.__name__}.{instance2.id}",
                      all_objects, "Second object in reloaded storage")

    def test_object_deletion(self):
        """Test deletion of an object."""
        instance = BaseModel()
        self.storage.new(instance)
        key = f"{instance.__class__.__name__}.{instance.id}"
        del self.storage.all()[key]  # Simulate deletion

        self.storage.save()
        self.storage.reload()
        self.assertNotIn(key, self.storage.all(),
                         "Deleted object not in storage after reload")

    def test_object_update(self):
        """Test object update."""
        instance = BaseModel()
        instance.name = "Test Name"
        self.storage.new(instance)
        self.storage.save()

        instance.name = "Updated Name"
        self.storage.save()
        self.storage.reload()

        reloaded_instance = self.storage.all()[
            f"{instance.__class__.__name__}.{instance.id}"]
        self.assertEqual(reloaded_instance.name, "Updated Name",
                         "Updated attribute saved and reloaded")

    def test_file_path_customization(self):
        """Test customization of the file path."""
        new_file_path = os.path.join(self.temp_dir, "test_file.json")
        FileStorage._FileStorage__file_path = new_file_path
        self.storage.save()

        self.assertTrue(os.path.exists(new_file_path),
                        "File created at new file path")
        os.remove(new_file_path)

    def test_data_integrity(self):
        """Test data integrity after save and reload."""
        instance = BaseModel()
        instance.name = "Test Name"
        self.storage.new(instance)
        self.storage.save()

        print("Current working directory:", os.getcwd())

        self.storage.reload()
        reloaded_instance = self.storage.all()[
            f"{instance.__class__.__name__}.{instance.id}"]
        self.assertEqual(reloaded_instance.name, "Test Name",
                         "Data intact after save and reload")

    def test_save_method_one(self):
        """Test the save method of FileStorage."""
        instance = BaseModel()
        self.storage.new(instance)  # Add object
        self.storage.save()

        # Check if file is created
        self.assertTrue(os.path.exists('file.json'), "File created on save")


if __name__ == '__main__':
    unittest.main()
