class Description:
    def __init__(self, id, name, link, salary, description, date_published):
        self.id = id
        self.name = name
        self.link = link
        self.salary = salary
        self.description = description
        self.date_published = date_published

    def __str__(self):
        return self.name

    def __lt__(self, other):
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
        return self.__lt__(other) or self.__eq__(other)

    @staticmethod
    def filter_with_salary(descriptions):
        filtered_descriptions = []
        for description in descriptions:
            if description.salary['from'] is not None:
                filtered_descriptions.append(description)
        return filtered_descriptions

    @staticmethod
    def sort_by_salary(descriptions):
        return sorted(descriptions, reverse=True)
