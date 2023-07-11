import json
from abc import ABC, abstractmethod
from src.description import Description


class Saver(ABC):
    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def add_descriptions(self, vacancies):
        pass

    @abstractmethod
    def delete_description(self, vacancy):
        pass


class JsonSaver(Saver):
    def __init__(self, path='descriptions.json'):
        self.path = path

    def read_file(self):
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
        descriptions = self.read_file()
        if isinstance(vacancies, Description):
            vacancies = [vacancies]
        for vacancy in vacancies:
            item = {
                'id': vacancy.id,
                'name': vacancy.name,
                'link': vacancy.link,
                'salary': vacancy.salary,
                'description': vacancy.description
            }
            descriptions.append(item)
        with open(self.path, 'w+', encoding='utf-8') as file:
            file.truncate(0)
            json.dump(descriptions, file)

    def delete_description(self, vacancy):
        descriptions = self.read_file()
        for i in range(len(descriptions)):
            if descriptions[i]['id'] == vacancy.id:
                print('deleted')
                del descriptions[i]
                break
        with open(self.path, 'w', encoding='utf-8') as file:
            file.truncate(0)
            json.dump(descriptions, file)

#json_saver = JSONSaver()
#json_saver.add_vacancy(vacancy)
#json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
#json_saver.delete_vacancy(vacancy)