#!/usr/bin/env python3
import client
import typing as t
import unittest
from parameterized import parameterized
from unittest.mock import (
    patch,
    MagicMock,
    PropertyMock
)


class TestGithubOrgClient(unittest.TestCase):
    """
    Implement test cases and test the client module
    """
    @parameterized.expand([
        ('test google', 'google', {'payload': 'google'}),
        ('test abc', 'abc', {'payload': 'abc'})
    ])
    @patch('client.get_json')
    def test_org(
        self,
        description: str,
        org: str,
        result: t.Dict,
        mock_method: MagicMock
    ) -> None:
        """
        Test client.GithubOrgClient.org
        """
        mock_method.return_value = result
        c = client.GithubOrgClient(org)
        first_call = c.org

        self.assertEqual(first_call, result)

        mock_method.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )

    def test_public_repos_url(self):
        """Test public_repos_url"""
        mock_org_payload = {
            'repos_url': 'https://api.github.com/orgs/test-org/repos'
        }

        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock,
            return_value=mock_org_payload
        ):
            c = client.GithubOrgClient('test-org')
            self.assertEqual(
                'https://api.github.com/orgs/test-org/repos',
                c._public_repos_url
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Test that public_repos returns the expected list of repos"""
        mock_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "gpl"}},
        ]

        mock_get_json.return_value = mock_repos_payload
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock,
            return_value='https://api.github.com/orgs/test-org/repos'
        ) as mock_repos_url:
            c = client.GithubOrgClient('test-org')
            repos = c.public_repos()
            self.assertEqual(repos, ['repo1', 'repo2', 'repo3'])

            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                'https://api.github.com/orgs/test-org/repos'
            )
