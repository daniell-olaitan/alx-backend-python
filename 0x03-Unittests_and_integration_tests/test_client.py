#!/usr/bin/env python3
"""
Implement test cases and test the client module
"""
import client
import typing as t
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import (
    patch,
    Mock,
    MagicMock,
    PropertyMock
)
from fixtures import TEST_PAYLOAD


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
        Test client.GithubOrgClient.org for correctness
        """
        mock_method.return_value = result
        c = client.GithubOrgClient(org)
        first_call = c.org

        self.assertEqual(first_call, result)

        mock_method.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )

    def test_public_repos_url(self):
        """Test public_repos_url for correctness"""
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

    @parameterized.expand([
        ('test 1', {"license": {"key": "my_license"}}, "my_license", True),
        ('test 2', {"license": {"key": "other_license"}}, "my_license", False),
        ('test 3', {"license": {"k": "other_license"}}, "my_license", False)
    ])
    def test_has_license(
        self,
        name: str,
        repo: t.Dict[str, t.Dict],
        key: str,
        result: bool
    ) -> None:
        """
        Test has_license method of the client module
        """
        self.assertEqual(
            client.GithubOrgClient.has_license(repo, key),
            result
        )


@parameterized_class([
    {
        'org_payload': payload[0],
        'repos_payload': payload[1],
        'expected_repos': payload[2],
        'apache2_repos': payload[3]
    }
    for payload in TEST_PAYLOAD
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Implement test cases and test the client module
    """
    @classmethod
    def side_effect(cls, url: str) -> t.Dict:
        """
        Mock side effect for requests.get
        """
        mock_response = Mock()

        if url == 'https://api.github.com/orgs/google':
            mock_response.json.return_value = cls.org_payload
        elif url == cls.org_payload['repos_url']:
            mock_response.json.return_value = cls.repos_payload
        else:
            mock_response.json.return_value = {}

        return mock_response

    @classmethod
    def setUpClass(cls):
        """
        Implement setup class for integration tests of GithubOrgClient
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = cls.side_effect

    @classmethod
    def tearDownClass(cls):
        """
        Implement teardown class for integration tests of GithubOrgClient
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos method of the client module
        """
        c = client.GithubOrgClient('google')
        self.assertEqual(c.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos method of the client module
        """
        c = client.GithubOrgClient('google')
        self.assertEqual(
            c.public_repos(license='apache-2.0'),
            self.apache2_repos
        )
