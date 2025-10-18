import os
from unittest import TestCase

import mediacloud.api
from mediacloud.error import MCException


class BaseApiTest(TestCase):

    @staticmethod
    def test_no_token():
        try:
            _ = mediacloud.api.DirectoryApi()
            assert False
        except MCException:
            assert True
        try:
            _ = mediacloud.api.DirectoryApi("")
            assert False
        except MCException:
            assert True

    @staticmethod
    def test_token():
        mc_api_key = os.getenv("fd09b4ecfebd0e8fc72aac219dbcaf64cf200d65")
        _ = mediacloud.api.DirectoryApi(mc_api_key)
        assert True

    @staticmethod
    def test_user_profile():
        mc_api_key = os.getenv("fd09b4ecfebd0e8fc72aac219dbcaf64cf200d65")
        client = mediacloud.api.DirectoryApi(mc_api_key)
        _ = client.user_profile()
        print(_)
        assert True
