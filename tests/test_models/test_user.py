#!/usr/bin/python3
"""Modules"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test methods testing for edge cases
    """
    def test_user_initialization(self):
        user = User()
        self.assertIsInstance(user, User,
                              "Should be an instance of User")
        self.assertEqual(user.email, "",
                         "email should be initialized as empty string")
        self.assertEqual(user.password, "",
                         "password should be initialized as empty string")
        self.assertEqual(user.first_name, "",
                         "first_name should be initialized as empty string")
        self.assertEqual(user.last_name, "",
                         "last_name should be initialized as empty string")


if __name__ == '__main__':
    unittest.main()
