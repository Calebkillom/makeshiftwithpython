#!/usr/bin/python3
""" still more unittest practise """
from __future__ import print_function
import unittest


class TestFail(unittest.TestCase):
    """TestFail class"""
    def test_false(self):
        """test_false method"""
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
