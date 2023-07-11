import json
from abc import ABC, abstractmethod
from src.description import Description


class Saver(ABC):
    '''
    Базовый класс для взаимодействия с файлами
    '''
    @abstractmethod
    def read_datafile(self):
        '''
        Метод для чтения файла
        '''
        pass

    @abstractmethod
    def add_descriptions(self, vacancies):
        '''
        Метод для добавления вакансий в файл
        '''
        pass

    @abstractmethod
    def delete_description(self, vacancy):
        '''
        Метод для удаления вакансии из файла
        '''
        pass

    @abstractmethod
    def get_by_keywords(self, keyword):
        '''
        Метод для получения вакансий из файла по ключевым словам
        '''
        pass


class JsonSaver(Saver):
    '''
    Класс для работы с файлами json
    Опциональный параметр path - путь к файлу.
    default path: descriptions.json
    '''
    def __init__(self, path='descriptions.json'):
        self.path = path

    def read_datafile(self):
        '''
        Возвращает список словарей с данными о вакансии,
        в формате класса Description
        Если файл пустой или отсутствует - возвращает пустой списко
        '''
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                text = file.read()
                if text:
                    return json.loads(text)
                else:
                    return []
        except FileNotFoundError:
            return []

    def add_descriptions(self, vacancies):
        '''
        Добавляет вакансии
        Принимает список экземпляров или экземпляр класса Description
        '''
        descriptions = self.read_datafile()
        if isinstance(vacancies, Description):
            vacancies = [vacancies]
        for vacancy in vacancies:
            item = {
                'id': vacancy.id,
                'name': vacancy.name,
                'link': vacancy.link,
                'salary': vacancy.salary,
                'description': vacancy.description,
                'date_published': vacancy.date_published
            }
            descriptions.append(item)
        with open(self.path, 'w', encoding='utf-8') as file:
            file.truncate(0)
            json.dump(descriptions, file)

    def delete_description(self, vacancy):
        '''
        Удаляет вакансию из файла.
        Принимает на вход экземпляр класса Description
        '''
        descriptions = self.read_datafile()
        for i in range(len(descriptions)):
            if descriptions[i]['id'] == vacancy.id:
                del descriptions[i]
                break
        with open(self.path, 'w', encoding='utf-8') as file:
            file.truncate(0)
            json.dump(descriptions, file)

    def get_by_keywords(self, keywords):
        '''
        Возвращает список вакансий, содержащих ВСЕ ключевые слова
        Принимает на вход строку ключевых слов, разделённых пробелами
        Формат возврата: список словарей
        '''
        descriptions = self.read_datafile()
        keywords = keywords.lower().split()
        filtered_descriptions = []
        for description in descriptions:
            found = True
            for keyword in keywords:
                if keyword in description['name'].lower() or keyword in description['description'].lower():
                    continue
                else:
                    found = False
                    break
            if found:
                filtered_descriptions.append(description)
        return filtered_descriptions
