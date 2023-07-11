import json
from abc import ABC, abstractmethod
from src.description import Description
import datetime


class Saver(ABC):
    @abstractmethod
    def read_datafile(self):
        pass

    @abstractmethod
    def add_descriptions(self, vacancies):
        pass

    @abstractmethod
    def delete_description(self, vacancy):
        pass

    @abstractmethod
    def get_by_keywords(self, keyword):
        pass


class JsonSaver(Saver):
    def __init__(self, path='descriptions.json'):
        self.path = path

    def read_datafile(self):
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
        descriptions = self.read_datafile()
        for i in range(len(descriptions)):
            if descriptions[i]['id'] == vacancy.id:
                print('deleted')
                del descriptions[i]
                break
        with open(self.path, 'w', encoding='utf-8') as file:
            file.truncate(0)
            json.dump(descriptions, file)

    def get_by_keywords(self, keywords):
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
