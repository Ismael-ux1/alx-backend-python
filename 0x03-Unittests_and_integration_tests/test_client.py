#!/usr/bin/env python3
""" Parameterize and patch as decorators """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get):
        """Test that GithubOrgClient.org returns the correct value"""
        mock_get.return_value = {"name": org_name}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {"name": org_name})
        mock_get.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
        )
