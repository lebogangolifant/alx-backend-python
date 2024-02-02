#!/usr/bin/env python3
"""
Module contains unit tests for client.GithubOrgClient.
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Class contains unit tests for client.GithubOrgClient.
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', autospec=True)
    def test_org(self, org_name, mock_get_json):
        """
        Method to test org of GithubOrgClient
        """
        expected_result = {org_name: True}
        mock_get_json.return_value = expected_result
        github_org_client = GithubOrgClient(org_name)

        result = github_org_client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_result)

    def test_public_repos_url(self):
        """
        Test _public_repos_url method of GithubOrgClient
        """
        expected = 'https://api.github.com/orgs/testorg/repos'
        cli = GithubOrgClient('testorg')

        result = cli._public_repos_url

        self.assertEqual(result, expected)

    @patch('client.GithubOrgClient.get_json', return_value=[
           {'name': 'repo1'}, {'name': 'repo2'}])
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock,
           return_value='https://api.github.com/orgs/testorg/repos')
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test public_repos method of GithubOrgClient
        """
        expected_repos = [{'name': 'repo1'}, {'name': 'repo2'}]
        cli = GithubOrgClient('testorg')

        result = cli.public_repos

        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
                'https://api.github.com/orgs/testorg/repos')
        self.assertEqual(result, expected_repos)
