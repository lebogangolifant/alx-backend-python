#!/usr/bin/env python3
"""
Unit tests module for utils.access_nested_map.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Class contains unit tests for utils.access_nested_map.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Ensure access_nested_map returns the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
       ({}, ("a",), KeyError, "Key 'a' not found"),
       ({"a": 1}, ("a", "b"), KeyError, "Key 'b' not found"),
    ])
    def test_nested_map_exception(self, nested, path, expected_exc,
                                  expected_msg):
        """
        Ensure access_nested_map raises the expected exception.
        """
        with self.assertRaises(expected_exc, msg=expected_msg):
            access_nested_map(nested, path)


class TestGetJson(unittest.TestCase):
    """
    Class contains unit tests for utils.get_json.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Ensure get_json returns the expected result using unittest.mock.patch.
        """
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
