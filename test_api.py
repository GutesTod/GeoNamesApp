import unittest, requests
from random import randint

class TestRESTApi(unittest.TestCase):

    def test_api_geonameid(self):
        codesnameid = ['451854', '10106491', '10106656', '10110478']
        for codenameid in codesnameid:
            assert requests.get(f"http://127.0.0.1:8000/api/city/{codenameid}")
    
    def test_api_pages(self):
        for iter in range(5):
            start = randint(1,5)
            end = randint(10, 25)
            assert requests.get(f'http://127.0.0.1:8000/api/cities?page={start}&per_page={end}')

    def test_api_search_city(self):
        cities = ['Выходный', 'Выборг', 'Москва', 'Улан-Удэ', 'Уфа', 'Воронеж', 'Воробьевка', 'Санкт-Петербуг', 'Волонтер']
        for i in range(1, len(cities)):
            try:
                assert requests.get(f'http://127.0.0.1:8000/two-cities?city1_name={cities[i]}&city2_name={cities[i-1]}')
            except AssertionError:
                print(requests.get(f'http://127.0.0.1:8000/two-cities?city1_name={cities[i]}&city2_name={cities[i-1]}'))
        