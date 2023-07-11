import requests
from abc import ABC, abstractmethod
from api_key import SJ_KEY


class Api(ABC):
    @abstractmethod
    def get_info(self, key):
        pass

    @abstractmethod
    def output_info(self, key):
        pass


class HeadHunter(Api):
    def __init__(self):
        pass

    def get_info(self, key):
        params = {"area": 113, "text": key, "per_page": 10}
        response = requests.get('https://api.hh.ru/vacancies', params)
        print(response.json())
        assert response.status_code == 200
        return response.json()['items']

    def output_info(self, key):
        hh_output = self.get_info(key)
        output = []
        for info in hh_output:
            id = int(info['id'])
            name = info['name']
            link = info['alternate_url']
            if info['salary'] is not None:
                salary = {
                    'from': info['salary']['from'],
                    'to': info['salary']['to']
                }
            else:
                salary = {'from': None, 'to': None}
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
    api_key = SJ_KEY
    header = {'X-Api-App-Id': api_key}

    def __init__(self):
        pass

    def get_info(self, key):
        params = {'keyword': key}
        response = requests.get('https://api.superjob.ru/2.0/vacancies', params, headers=self.header)
        assert response.status_code == 200
        items = response.json()['objects']
        return items

    def output_info(self, key):
        superjob = self.get_info(key)
        output = []
        for info in superjob:
            id = int(info['id'])
            name = info['profession']
            link = info['link']
            salary = {}
            salary['from'] = info['payment_from'] if info['payment_from'] else None
            salary['to'] = info['payment_to'] if info['payment_to'] else None

            description = info['candidat']
            item = {
                'id': id,
                'name': name,
                'link': link,
                'salary': salary,
                'description': description
            }
            output.append(item)
        return output
