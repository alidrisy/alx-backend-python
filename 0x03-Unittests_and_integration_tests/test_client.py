#!/usr/bin/env python3
""" Model for client model methods """
from parameterized import parameterized
from client import GithubOrgClient
from typing import Callable, Mapping
from unittest.mock import patch, PropertyMock
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ Class to test GithubOrgClient model """

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, result: Mapping, get_json: Callable):
        """test that GithubOrgClient.org returns the correct value."""
        get_json.return_value = result
        git_hub_org = GithubOrgClient(org_name)
        resp = git_hub_org.org
        self.assertEqual(result, resp)
        resp = git_hub_org.org
        get_json.assert_called_once()

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc"})
    ])
    def test_public_repos_url(self, org_name: str, result: Mapping):
        """Test that the result of _public_repos_url is the expected
        one based on the mocked payload."""
        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock) as org:
            org.return_value = result
            git_hub_org = GithubOrgClient(org_name)
            resp = git_hub_org._public_repos_url
            self.assertEqual(result["repos_url"], resp)


if __name__ == "__main__":
    unittest.main()
