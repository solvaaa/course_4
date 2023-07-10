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
        if (self.salary is not None) and (self.salary['from'] is not None):
            if (other.salary is not None) and (other.salary['from'] is not None):
                return self.salary['from'] < other.salary['from']
            else:
                return False
        elif (other.salary is not None) and (other.salary['from'] is not None):
            return True
        else:
            return False

    def __eq__(self, other):
        if (self.salary is not None) and (other.salary is not None):
            return self.salary['from'] == other.salary['from']