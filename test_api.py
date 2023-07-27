import unittest
import requests

class TestRESTApi(unittest.TestCase):

    def test_api_geonameid(self):
        assert requests.get("http://127.0.0.1:8000/api/cities/451854")
        assert requests.get("http://127.0.0.1:8000/api/cities/10106491")
        assert requests.get("http://127.0.0.1:8000/api/cities/10106656")