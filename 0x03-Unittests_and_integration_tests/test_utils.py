#!/usr/bin/env python3
""" Model for utils model methods """
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from unittest.mock import patch
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
        """ test that the access_nested_map method return the right value """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """ test that the access_nested_map method
        raise keyError for the parameterized inputs """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class to test utils get_json method """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Mapping) -> None:
        """test that utils.get_json returns the expected result."""
        with patch("requests.get") as mock_get:
            mock_response = mock_get.return_value
            mock_response.json.return_value = test_payload
            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Class to test utils memoize method """

    def test_memoize(self):
        """test that when calling a_property twice, the correct result is
        returned but a_method is only called once using assert_called_once."""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as a_method:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
