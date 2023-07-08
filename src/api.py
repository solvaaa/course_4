import requests
import json
from abc import ABC, abstractmethod


class Api(ABC):
    @abstractmethod
    def get_info(self, key):
        pass


class HeadHunter(Api):
    def __init__(self):
        pass

    def get_info(self, key):
        params = {"area": 113, "text": key, "per_page": 10}
        response = requests.get('https://api.hh.ru/vacancies', params)
        print(*response.json()['items'], sep='\n')


class SuperJob(Api):
    def __init__(self):
        pass

    def get_info(self, key):
        pass


hh = HeadHunter()
hh.get_info('Python-разработчик')