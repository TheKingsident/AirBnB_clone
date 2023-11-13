#!/usr/bin/python3
"""Modules"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test methods testing for edge cases
    """
    def test_place_initialization(self):
        place = Place()
        self.assertIsInstance(place, Place,
                              "Should be an instance of Place")
        self.assertEqual(place.city_id, "",
                         "city_id should be initialized as empty string")
        self.assertEqual(place.user_id, "",
                         "user_id should be initialized as empty string")
        # Continue for other attributes...


if __name__ == '__main__':
    unittest.main()
