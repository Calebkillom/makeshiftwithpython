#!/usr/bin/python3
"""Pass arguments into a TestCase"""
from __future__ import print_function
import unittest


class TestArg(unittest.TestCase):
    """Test Argument Class"""
    def __init__(self, testname, arg):
        """initialisation method"""
        super(TestArg, self).__init__(testname)
        self._arg = arg

    def setUp(self):
        """setUp Method"""
        print("setUp:", self._arg)

    def test_arg(self):
        """test_arg method"""
        print("test_arg:", self._arg)
        self.assertTrue(True)


suite = unittest.TestSuite()
suite.addTest(TestArg('test_arg', 'foo'))
unittest.TextTestRunner(verbosity=2).run(suite)
