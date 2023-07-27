import unittest, requests
from random import randint

class TestRESTApi(unittest.TestCase):

    def test_api_geonameid(self):
        codesnameid = ['451854', '10106491', '10106656', '1', '2', '10110478']
        for codenameid in codesnameid:
            assert requests.get(f"http://127.0.0.1:8000/api/city/{codenameid}")
    
    def test_api_pages(self):
        for iter in range(5):
            start = randint(1,5)
            end = randint(10, 25)
            assert requests.get(f'http://127.0.0.1:8000/api/cities?page={start}&per_page={end}')