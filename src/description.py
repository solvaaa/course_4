class Description:
    def __init__(self, id, name, link, salary, description):
        self.id = id
        self.name = name
        self.link = link
        self.salary = salary
        self.description = description

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
