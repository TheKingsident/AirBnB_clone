#!/usr/bin/python3
"""Modules"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test methods testing for edge cases
    """
    def test_review_initialization(self):
        review = Review()
        self.assertIsInstance(review, Review,
                              "Should be an instance of Review")
        self.assertEqual(review.place_id, "",
                         "place_id should be initialized as empty string")
        self.assertEqual(review.user_id, "",
                         "user_id should be initialized as empty string")
        self.assertEqual(review.text, "",
                         "text should be initialized as empty string")


if __name__ == '__main__':
    unittest.main()
