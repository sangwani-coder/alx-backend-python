#!/usr/bin/env python3
""" utils test module"""
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ test case"""
    @parameterized.expand([
        ({'a': 1}, ('a'), 1),
        ({'a': {'b': 2}}, ('a'), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test single map with single path"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a'), KeyError('a')),
        ({'a': 1}, ('a', 'b'), KeyError('b'))
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ raise exception with invalid arguments"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map=nested_map, path=path)

        self.assertEqual(repr(error.exception), repr(expected))


if __name__ == "__main__":
    unittest.main()
