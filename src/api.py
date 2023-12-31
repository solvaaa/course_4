import requests
import os
from abc import ABC, abstractmethod
from api_key import SJ_KEY
import datetime


class Api(ABC):
    '''
    Базовый класс для работы с API сайтов по поиску работы
    '''
    @abstractmethod
    def get_info(self, key):
        '''
        Метод для получения сырой информации из API по ключевому слову.
        Возвращает список словарей
        '''
        pass

    @abstractmethod
    def output_info(self, key):
        '''
        Метод возвращает отформатированную информацию о вакансиях
        по ключевому слову.
        Содержит следующие поля:
        id, name, link, salary, description, date_published
        salary - словарь с ключами to и from
        '''
        pass


class HeadHunter(Api):
    '''
    Класс для получения информации из API HeadHunter.ru
    '''
    def __init__(self, per_page=100):
        '''
        :param per_page: задаёт количество запрашиваемых вакансий. До 100
        '''
        self.per_page = per_page

    def get_info(self, key):
        '''
        Метод для получения сырой информации из API по ключевому слову.
        Возвращает список словарей
        '''
        params = {"area": 113, "text": key, "per_page": self.per_page}
        response = requests.get('https://api.hh.ru/vacancies', params)
        assert response.status_code == 200, 'Request not successful'
        return response.json()['items']

    def output_info(self, key):
        '''
        Метод возвращает отформатированную информацию о вакансиях
        по ключевому слову.
        Содержит следующие поля:
        id, name, link, salary, description, date_published
        salary - словарь с ключами to и from
        '''
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
                        value = value.replace('<highlighttext>', '')
                        value = value.replace('</highlighttext>', '')
                        snippet.append(value)
                description = ' '.join(snippet)
            else:
                description = None

            date_raw = info['published_at']
            date_published = datetime.datetime.strptime(date_raw, '%Y-%m-%dT%H:%M:%S%z')
            date_published = datetime.datetime.replace(date_published, tzinfo=None)
            date_published = date_published.strftime('%Y-%m-%d %H:%M:%S')
            item = {
                'id': id,
                'name': name,
                'link': link,
                'salary': salary,
                'description': description,
                'date_published': date_published
            }
            output.append(item)
        return output


class SuperJob(Api):
    '''
    Класс для получения информации из API SuperJob.ru
    '''
    api_key = os.getenv('SJ_KEY')
    if api_key is None:
        api_key = SJ_KEY
    header = {'X-Api-App-Id': api_key}

    def __init__(self, per_page=100):
        self.per_page = per_page

    def get_info(self, key):
        '''
        Метод для получения сырой информации из API по ключевому слову.
        Возвращает список словарей
        '''
        params = {'keyword': key, 'currency': 'rub', 'count': 100}
        response = requests.get('https://api.superjob.ru/2.0/vacancies', params, headers=self.header)
        assert response.status_code == 200, 'Request not successful'
        items = response.json()['objects']
        return items

    def output_info(self, key):
        '''
        Метод возвращает отформатированную информацию о вакансиях
        по ключевому слову.
        Содержит следующие поля:
        id, name, link, salary, description, date_published
        salary - словарь с ключами to и from
        '''
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

            date_raw = info['date_published']
            date_published = datetime.datetime.fromtimestamp(date_raw)
            date_published = date_published.strftime('%Y-%m-%d %H:%M:%S')

            item = {
                'id': id,
                'name': name,
                'link': link,
                'salary': salary,
                'description': description,
                'date_published': date_published
            }
            output.append(item)
        return output
