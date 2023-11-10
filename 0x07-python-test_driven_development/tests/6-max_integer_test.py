#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class that contains test cases for testing the maximum integer
        of max_integer function
    """
    def test_max_integer(self):
        self.assertEqual(max_integer([2, 9, 0, -4]), 9)
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([3, 3, 9, 9, -1]), 9)
