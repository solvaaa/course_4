import json
from abc import ABC, abstractmethod


class Saver(ABC):
    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def add_description(self):
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



#json_saver = JSONSaver()
#json_saver.add_vacancy(vacancy)
#json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
#json_saver.delete_vacancy(vacancy)