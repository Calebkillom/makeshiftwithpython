#!/usr/bin/python3
"""Python unittest setup & teardown hierarchy"""
from __future__ import print_function
import unittest


def fib(n):
    """fibonacci function"""
    return 1 if n <= 2 else fib(n - 1) + fib(n - 2)


def setUpModule():
    """setup module function"""
    print("setup module")


def tearDownModule():
    """teardown Module"""
    print("Teardown Module")


class TestFib(unittest.TestCase):
    """testing Fib function"""
    def setUp(self):
        """setup method"""
        print("setup!!!")
        self.n = 10

    def tearDown(self):
        """teardown method"""
        print("teardown")
        del self.n

    @classmethod
    def setUpClass(cls):
        """setup class method"""
        print("Setup Class")

    @classmethod
    def tearDownClass(cls):
        """teardown class method"""
        print("tearDownClass")

    def test_fib_assert_equal(self):
        """testing the actual fib func"""
        self.assertEqual(fib(self.n), 55)

    def test_fib_assert_true(self):
        """still testing fib function"""
        self.assertTrue(fib(self.n) == 55)


if __name__ == "__main__":
    unittest.main()
