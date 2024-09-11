#!/usr/bin/env python3
"""
Implement a unittest to test a method
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
import typing as t
import utils


class TestAccessNestedMap(unittest.TestCase):
    """
    Implement test cases and test utils.access_nested_map
    """
    @parameterized.expand([
        ('linear map, linear path', {"a": 1}, ("a",), 1),
        (
            'nested map (2nd order), linear path',
            {"a": {"b": 2}},
            ("a",),
            {'b': 2}
        ),
        (
            'nested map (2nd order), nested path (2nd order)',
            {"a": {"b": 2}},
            ("a", "b"),
            2
         )
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
        self.assertEqual(utils.access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ('empty map', {}, ("a",), KeyError, 'a'),
        ('too long path', {"a": 1}, ("a", "b"), KeyError, 'b')
    ])
    def test_access_nested_map_exception(
        self,
        description: str,
        nested_map: t.Mapping,
        path: t.Sequence,
        exception: KeyError,
        exc_message: str
    ) -> None:
        """
        Test the exception of utils.access_nested_map method

        Args:
            description: description of test
            nested_map: dictionary of maps
            path: sequence of paths
            exception: exception raised
            exc_message: exception message
        """
        with self.assertRaises(exception) as context:
            utils.access_nested_map(nested_map, path)

        self.assertEqual(context.exception.args[0], exc_message)


class TestGetJson(unittest.TestCase):
    """
    Implement a test case and test utils.get_json
    """
    @parameterized.expand([
        ('first test', 'http://example.com', {"payload": True}),
        ('second test', 'http://holberton.io', {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(
        self,
        name: str,
        test_url: str,
        test_payload: t.Mapping,
        mock_response_get: MagicMock
    ) -> None:
        """
        Test a method by mocking an HTTP call
        """
        mock_response_get.return_value.json.return_value = test_payload
        response = utils.get_json(test_url)
        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Implement a test case and test utils.memoize
    """
    def test_memoize(self):
        """
        Test the memoize function of the utils module
        """
        class TestClass:
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
            TestClass,
            'a_method',
            return_value=42
        ) as mock_method:
            obj = TestClass()
            first_result = obj.a_property
            second_result = obj.a_property

            self.assertEqual(first_result, 42)
            self.assertEqual(second_result, 42)

            mock_method.assert_called_once()
