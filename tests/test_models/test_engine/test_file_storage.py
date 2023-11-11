#!/usr/bin/python3
"""
This module is a unittest for the FileStorage class
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        FileStorage._FileStorage__objects = {}
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method(self):
        """Test the all method of FileStorage."""
        storage = FileStorage()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict, "all method should return a dictionary")

    def test_new_method(self):
        """Test the new method of FileStorage."""
        storage = FileStorage()
        instance = BaseModel()
        storage.new(instance)
        all_objects = storage.all()
        key = f"{instance.__class__.__name__}.{instance.id}"
        self.assertIn(key, all_objects, "New object should be added to storage")


    def test_save_method(self):
        """Test the save method of FileStorage."""
        storage = FileStorage()
        instance = BaseModel()
        storage.new(instance)
        storage.save()
        with open('file.json', 'r') as file:
            data = file.read()
            self.assertIn(instance.id, data, "Saved file should contain the new object's id")

    def test_reload_method(self):
        """Test the reload method of FileStorage."""
        storage = FileStorage()
        instance = BaseModel()
        storage.new(instance)
        storage.save()
        storage.reload()
        all_objects = storage.all()
        key = f"{instance.__class__.__name__}.{instance.id}"
        self.assertIn(key, all_objects, "Reloaded storage should contain the saved object")

    def test_file_creation(self):
        """Test file creation on save."""
        self.storage.new(BaseModel())
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path), "File should be created on save")

    def test_empty_file_handling(self):
        """Test handling of an empty file on reload."""
        open(self.file_path, 'a').close()  # Create an empty file
        try:
            self.storage.reload()
            self.assertTrue(True, "Empty file should be handled without errors")
        except Exception as e:
            self.fail(f"Reload should not fail with empty file: {e}")

    def test_file_overwrite_on_save(self):
        """Test file overwrite on save."""
        # First save
        instance = BaseModel()
        self.storage.new(instance)
        self.storage.save()

        # Modify and save again
        instance.name = "New Name"
        self.storage.save()

        with open(self.file_path, 'r') as f:
            content = f.read()
            self.assertIn("New Name", content, "File should be overwritten on save")

    def test_invalid_data_handling_in_reload(self):
        """Test handling of invalid data in file on reload."""
        with open(self.file_path, 'w') as f:
            f.write("Invalid JSON")

        try:
            self.storage.reload()
            self.assertTrue(True, "Invalid data should be handled without crashing")
        except json.JSONDecodeError:
            self.fail("Reload should handle JSON decode errors gracefully")

    def test_nonexistent_file_handling(self):
        """Test handling of nonexistent file on reload."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        try:
            self.storage.reload()
            self.assertTrue(True, "Nonexistent file should be handled without errors")
        except FileNotFoundError:
            self.fail("Reload should not fail if the file does not exist")

    def test_save_with_multiple_objects(self):
        """Test saving multiple objects."""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.storage.new(instance1)
        self.storage.new(instance2)
        self.storage.save()

        with open(self.file_path, 'r') as f:
            content = f.read()
            self.assertIn(instance1.id, content, "File should contain the first object's id")
            self.assertIn(instance2.id, content, "File should contain the second object's id")

    def test_reload_with_multiple_objects(self):
        """Test reloading multiple objects."""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.storage.new(instance1)
        self.storage.new(instance2)
        self.storage.save()

        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn(f"{instance1.__class__.__name__}.{instance1.id}", all_objects, "Reloaded storage should contain the first object")
        self.assertIn(f"{instance2.__class__.__name__}.{instance2.id}", all_objects, "Reloaded storage should contain the second object")

    def test_object_deletion(self):
        """Test deletion of an object."""
        instance = BaseModel()
        self.storage.new(instance)
        key = f"{instance.__class__.__name__}.{instance.id}"
        del self.storage.all()[key]  # Simulate object deletion

        self.storage.save()
        self.storage.reload()
        self.assertNotIn(key, self.storage.all(), "Deleted object should not be in storage after reload")

    def test_object_update(self):
        """Test object update."""
        instance = BaseModel()
        instance.name = "Test Name"
        self.storage.new(instance)
        self.storage.save()

        instance.name = "Updated Name"
        self.storage.save()
        self.storage.reload()

        reloaded_instance = self.storage.all()[f"{instance.__class__.__name__}.{instance.id}"]
        self.assertEqual(reloaded_instance.name, "Updated Name", "Updated attribute should be saved and reloaded correctly")

    def test_file_path_customization(self):
        """Test customization of the file path."""
        new_file_path = "test_file.json"
        FileStorage._FileStorage__file_path = new_file_path
        self.storage.save()

        self.assertTrue(os.path.exists(new_file_path), "File should be created at the new file path")
        os.remove(new_file_path)

    def test_data_integrity(self):
        """Test data integrity after save and reload."""
        instance = BaseModel()
        instance.name = "Test Name"
        self.storage.new(instance)
        self.storage.save()
        print("Current working directory:", os.getcwd())

        self.storage.reload()
        reloaded_instance = self.storage.all()[f"{instance.__class__.__name__}.{instance.id}"]
        self.assertEqual(reloaded_instance.name, "Test Name", "Data should remain intact after save and reload")

    def test_save_method_one(self):
        """Test the save method of FileStorage."""
        instance = BaseModel()
        self.storage.new(instance)  # Ensure an object is added
        self.storage.save()

        # Then check if the file is created
        self.assertTrue(os.path.exists('file.json'), "File should be created on save")


if __name__ == '__main__':
    unittest.main()
