#!/usr/bin/python3
""" Test raise exception """
import unittest


class TestRaiseException(unittest.TestCase):
    """TestRaiseException Class"""
    def test_raise_except(self):
        """test_raise unittest"""
        with self.assertRaises(SystemError):
            raise SystemError


suite_loader = unittest.TestLoader()
suite = suite_loader.loadTestsFromTestCase(TestRaiseException)
unittest.TextTestRunner().run(suite)
