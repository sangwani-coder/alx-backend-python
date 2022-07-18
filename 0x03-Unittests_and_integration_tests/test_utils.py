#!/usr/bin/env python3
""" utils test module"""

import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ test case"""

    def test_single_map(self):
        """test single map with single path"""
        nested_map = {"a": 1}, path = ("a",)
        self.assertEqual(access_nested_map(nested_map, path), 1)

    def test_test_nested_map(self):
        """test nested map with single path
        nested_map={"a": {"b": 2}}, path=("a",)
        """
        pass

    def test_nested_map_single_path(self):
        """ nested map paths
        nested_map={"a": {"b": 2}}, path=("a", "b")
        """
        pass



if __name__ == "__main__":
    unittest.main()