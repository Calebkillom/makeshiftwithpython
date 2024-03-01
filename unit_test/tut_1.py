#!/usr/bin/python3
""" simple unittest practise"""

from __future__ import print_function
import unittest


class TestFoo(unittest.TestCase):
    """TEST FOO class"""
    def test_foo(self):
        """test foo method"""
        self.assertTrue(True)

    def fun_not_run(self):
        """ Another one"""
        print("no run")


if __name__ == '__main__':
    unittest.main()
