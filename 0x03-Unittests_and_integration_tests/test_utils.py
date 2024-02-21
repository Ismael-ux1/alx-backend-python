#!/usr/bin/env python3
""" Parameterize Unittests """
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Tuple, Dict


class TestAccessNestedMap(unittest.TestCase):
    """
    This is a class that contains unit tests for the,
    utils.access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any],
                               path: Tuple[str], expected: Any) -> None:
        """ nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a", "a"),
        ({"a": 1}, ("a", "b"), "b", "b")
    ])
    def test_access_nested_map_exception(self, _, nested_map, path, expected):
        """
        This is a context manager that checks,
        if the function raises a KeyError with the,
        expected message for each input
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(expected))
