#!/usr/bin/python3
"""
Different module of setUp & tearDown hierarchy
"""
from __future__ import print_function
import unittest


class TestFoo(unittest.TestCase):
    """Class TestFoo"""
    @classmethod
    def setUpClass(self):
        """Setup Class"""
        print("foo Setup Class")

    @classmethod
    def tearDownClass(self):
        """tearDownClass"""
        print("foon tearDownClass")

    def setUp(self):
        """setUp method"""
        print("foo setUp")

    def tearDown(self):
        """tearDown Method"""
        print("foo TearDown")

    def test_foo(self):
        """the actual testing of the foo function"""
        self.assertTrue(True)


class TestBar(unittest.TestCase):
    """TestBar Class"""
    def setUp(self):
        """setUp method"""
        print("bar setUp")

    def tearDown(self):
        """tearDown method"""
        print("bar tearDown")

    def test_bar(self):
        """actual testing of TestBar"""
        self.assertTrue(True)
