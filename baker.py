class Bakery:
    
    def __init__(self, name):
        self.__name = name
        self.__pantry = {}

    def __add__(self, ingredients):
        for i in ingredients:
            self.__pantry[i] = ingredients[i]
        return self

    @property
    def name(self):
        return self.__name
    
    @property
    def pantry(self):
        return self.__pantry

