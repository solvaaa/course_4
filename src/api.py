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
        return response.json()['items']

    def output_info(self, key):
        hh_output = self.get_info(key)
        output = []
        for info in hh_output:
            id = info['id']
            name = info['name']
            link = info['alternate_url']
            if info['salary'] is not None:
                salary = {
                    'from': info['salary']['from'],
                    'to': info['salary']['to']
                }
            else:
                salary = None
            if info['snippet'] is not None:
                snippet = []
                for key, value in info['snippet'].items():
                    if value is not None:
                        snippet.append(value)
                description = ' '.join(snippet)
            else:
                description = None
            item = {
                'id': id,
                'name': name,
                'link': link,
                'salary': salary,
                'description': description
            }
            output.append(item)
        return output


class SuperJob(Api):
    def __init__(self):
        pass

    def get_info(self, key):
        pass


hh = HeadHunter()
output = hh.output_info('Python-разработчик')
print(*output, sep='\n')
