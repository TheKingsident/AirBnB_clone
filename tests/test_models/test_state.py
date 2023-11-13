#!/usr/bin/python3
"""Modules"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Test methods testing for edge cases
    """
    def test_state_initialization(self):
        state = State()
        self.assertIsInstance(state, State,
                              "Should be an instance of State")
        self.assertEqual(state.name, "",
                         "name should be initialized as empty string")


if __name__ == '__main__':
    unittest.main()
