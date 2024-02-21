#!/usr/bin/env python3
""" Parameterize and patch as decorators """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import PropertyMock


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

    def test_public_repos_url(self):
        """
        Test that GithubOrgClient._public_repos_url returns the correct URL
        """
        # Define a test payload for the organization
        test_payload = {
                "repos_url": "https://api.github.com/orgs/google/repos"
                }

        # Use patch as a context manager to mock the org property
        with patch.object(
                GithubOrgClient, "org", new_callable=PropertyMock
                ) as mock_org:
            # Configure the mock property to return the test payload
            mock_org.return_value = test_payload

            # Create an instance of the GithubOrgClient,
            # class with a test organization name
            client = GithubOrgClient("google")

            # Test that the _public_repos_url method returns the expected URL
            self.assertEqual(
                    client._public_repos_url, test_payload["repos_url"]
                    )
