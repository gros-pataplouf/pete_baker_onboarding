class Bakery:
    
    def __init__(self, name):
        self.__name = name
        self.__pantry = {}

    def __add__(self, ingredients):
        for i in ingredients:
            self.__pantry[i] = self.__pantry.get(i, 0) + ingredients[i]
        return self

    @property
    def name(self):
        return self.__name
    
    @property
    def pantry(self):
        return self.__pantry

    def use(self, needed_ingredients : dict) -> dict :
        for i in needed_ingredients:
            self.__pantry[i] -= needed_ingredients[i]
        return needed_ingredients