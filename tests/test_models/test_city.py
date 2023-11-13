#!/usr/bin/python3
"""Modules"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):

    def test_city_initialization(self):
        city = City()
        self.assertIsInstance(city, City,
                              "Should be an instance of City")
        self.assertEqual(city.state_id, "",
                         "state_id should be initialized as empty string")
        self.assertEqual(city.name, "",
                         "name should be initialized as empty string")


if __name__ == '__main__':
    unittest.main()
