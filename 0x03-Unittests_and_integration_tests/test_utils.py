#!/usr/bin/env python3
""" Model for TestAccessNestedMap object """
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence, Any
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ Class to test utils.access_nested_map method """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, result: Any) -> None:
        """ test that the utils.access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), result)


if __name__ == "__main__":
    unittest.main()
