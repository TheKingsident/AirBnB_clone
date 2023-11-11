#!/usr/bin/python3
"""
This module is a unittest for the BaseModel class
"""
from models.base_model import BaseModel
import unittest
from datetime import datetime
from datetime import timedelta

class TestBaseModel(unittest.TestCase):

    def test_initialization(self):
        """Test the initialization of BaseModel without kwargs."""
        instance = BaseModel()
        self.assertIsNotNone(instance.id, "id should not be None")
        self.assertTrue(isinstance(instance.created_at, datetime), "created_at should be a datetime object")
        self.assertTrue(isinstance(instance.updated_at, datetime), "updated_at should be a datetime object")

        time_diff = instance.updated_at - instance.created_at
        self.assertTrue(time_diff < timedelta(seconds=1), "created_at and updated_at should be almost equal at initialization")

    def test_initialization_with_kwargs(self):
        """Test the initialization of BaseModel with kwargs."""
        kwargs = {
            'id': '123',
            'created_at': '2021-01-01T00:00:00.000000',
            'updated_at': '2021-01-02T00:00:00.000000'
        }
        instance = BaseModel(**kwargs)
        self.assertEqual(instance.id, '123', "id should match the one provided in kwargs")
        self.assertEqual(instance.created_at.isoformat(timespec='microseconds'), kwargs['created_at'], "created_at should match the one provided in kwargs")
        self.assertEqual(instance.updated_at.isoformat(timespec='microseconds'), kwargs['updated_at'], "updated_at should match the one provided in kwargs")

    def test_string_representation(self):
        """Test the string representation of BaseModel."""
        instance = BaseModel()
        expected_str = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(instance.__str__(), expected_str, "String representation should match the expected format")

    def test_save_method(self):
        """Test the save method of BaseModel."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(instance.updated_at, old_updated_at, "updated_at should be updated after save")

    def test_dictionary_conversion(self):
        """Test the dictionary conversion of BaseModel."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel', "__class__ key should be 'BaseModel'")
        self.assertEqual(instance_dict['id'], instance.id, "id in dictionary should match instance's id")
        self.assertIsInstance(instance_dict['created_at'], str, "created_at should be a string")
        self.assertIsInstance(instance_dict['updated_at'], str, "updated_at should be a string")

    def test_uuid_uniqueness(self):
        """Test the UUID uniqueness of BaseModel instances."""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id, "Each instance should have a unique id")

    def test_datetime_types(self):
        """Test the type of datetime attributes."""
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime, "created_at should be a datetime object")
        self.assertIsInstance(instance.updated_at, datetime, "updated_at should be a datetime object")

    def test_update_on_save(self):
        """Test that 'save' method updates 'updated_at' without changing 'created_at'."""
        instance = BaseModel()
        old_created_at = instance.created_at
        old_updated_at = instance.updated_at
        instance.save()
        self.assertEqual(instance.created_at, old_created_at, "'created_at' should not change on save")
        self.assertNotEqual(instance.updated_at, old_updated_at, "'updated_at' should be updated on save")

    def test_attribute_mutation(self):
        """Test the addition and modification of attributes."""
        instance = BaseModel()
        instance.name = "Test Name"
        instance.number = 42
        self.assertEqual(instance.name, "Test Name", "New attributes should be added correctly")
        self.assertEqual(instance.number, 42, "New attributes should be added correctly")
        instance.number = 43
        self.assertEqual(instance.number, 43, "Attributes should be modifiable")

    def test_invalid_kwargs_handling(self):
        """Test initialization with both valid and invalid kwargs."""
        kwargs = {
            'nonexistent_field': 'value',
            'id': '123',
            'created_at': '2021-01-01T00:00:00',
            'updated_at': '2021-01-02T00:00:00'
        }
        instance = BaseModel(**kwargs)
        self.assertTrue(hasattr(instance, 'nonexistent_field'), "Instance should handle dynamic attribute assignment")
        self.assertEqual(instance.id, '123', "Valid kwargs should be handled correctly")




if __name__ == '__main__':
    unittest.main()
