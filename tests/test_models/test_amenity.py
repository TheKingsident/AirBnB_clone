#!/usr/bin/python3
"""Modules"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_amenity_initialization(self):
        """Test the initialization of the Amenity class."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity,
                              "Should be an instance of Amenity")
        self.assertEqual(amenity.name, "",
                         "name should be initialized as an empty string")


if __name__ == '__main__':
    unittest.main()
