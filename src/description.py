class Description:
    def __init__(self, id, name, link, salary, description, date_published):
        '''
        Класс для работы с описаниями вакансий
        :param id: id вакансии. Целочисленный
        :param name: название вакансии
        :param link: ссылка на вакансию
        :param salary: зарплата. Словарь с ключами 'to' and 'from'
        :param description: Описание вакансии
        :param date_published: Дата публикации в виде строки
        '''
        self.id = id
        self.name = name
        self.link = link
        self.salary = salary
        self.description = description
        self.date_published = date_published

    def __str__(self):
        return self.name

    def __lt__(self, other):
        '''
        Сравнение ведётся по нижней границы зарплаты.
        Вакансии с отсутствующей минимальной зарплатой - наименьшие
        '''
        if self.salary['from'] is not None:
            if other.salary['from'] is not None:
                return self.salary['from'] < other.salary['from']
            else:
                return False
        else:
            return other.salary['from'] is not None

    def __eq__(self, other):
        return self.salary['from'] == other.salary['from']

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        '''
        Сравнение ведётся по нижней границы зарплаты.
        Вакансии с отсутствующей минимальной зарплатой - наименьшие
        '''
        return self.__lt__(other) or self.__eq__(other)

    @staticmethod
    def filter_with_salary(descriptions):
        '''
        Принимает список эксземпляров собственного класса.
        Возвращает список вакансий, где присутсвует минимальная зарплата
        '''
        filtered_descriptions = []
        for description in descriptions:
            if description.salary['from'] is not None:
                filtered_descriptions.append(description)
        return filtered_descriptions

    @staticmethod
    def sort_by_salary(descriptions):
        '''
        Принимает список эксземпляров собственного класса.
        Возвращает список экземпляров, отсортированных по минимальной зарплате (по убыванию)
        '''
        return sorted(descriptions, reverse=True)

    @staticmethod
    def sort_by_date(descriptions):
        '''
        Принимает список эксземпляров собственного класса.
        Возвращает список экземпляров, отсортированных по дате публикации (по убыванию)
        '''
        return sorted(descriptions, key=lambda x: x.date_published, reverse = True)
