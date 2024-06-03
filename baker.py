class Bakery:
    def __init__(self, name):
        self.__name = name
        self.__pantry = {}
    @property
    def name(self):
        return self.__name
    @property
    def pantry(self):
        return self.__pantry
