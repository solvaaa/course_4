class Description:
    def __init__(self, id, name, link, salary, description):
        self.id = id
        self.name = name
        self.link = link
        self.salary = salary
        self.description = description

    def __str__(self):
        return self.name

