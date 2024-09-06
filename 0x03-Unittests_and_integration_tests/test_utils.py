#!/usr/bin/env python3
"""
Implement a unittest to test a method
"""
import unittest
from parameterized import parameterized
import typing as t
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ('first_test', {"a": 1}, ("a",), 1),
        ('second_test', {"a": {"b": 2}}, ("a",), {'b': 2}),
        ('third_test', {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        name: str,
        nested_map: t.Mapping,
        path: t.Sequence,
        result: t.Union[t.Mapping, t.Any]
    ) -> None:
        """
        Test utils.access_nested_map method

        Args:
            name: name of test
            nested_map: dictionary of maps
            path: sequence of paths
            result: result of the
        """
        self.assertEqual(access_nested_map(nested_map, path), result)
