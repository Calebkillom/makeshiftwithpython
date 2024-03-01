#!/usr/bin/python3
""" testing module """
from __future__ import print_function
from test_module import TestFoo
from test_module import TestBar
import test_module
import unittest


def setUpModule():
    """setup function"""
    print("setUpModule")


def tearDownModule():
    """tearDownmodule"""
    print("tearDownModule")


if __name__ == "__main__":
    test_module.setUpModule = setUpModule
    test_module.tearDownModule = tearDownModule
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestFoo)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestBar)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner().run(suite)
