from abc import ABC, abstractmethod

class Api(ABC):
    @abstractmethod
    def get_info(self, key):
        pass

class HeadHunter(Api):
    def __init__(self):
        pass

    def get_info(self, key):
        pass


class SuperJob(Api):
    def __init__(self):
        pass

    def get_info(self, key):
        pass