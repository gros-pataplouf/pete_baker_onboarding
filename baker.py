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
        unavailable_ingredients = list(filter(lambda ingredient: self.__pantry[ingredient] <= needed_ingredients[ingredient], needed_ingredients))
        if not unavailable_ingredients:
            for i in needed_ingredients:
                self.__pantry[i] -= needed_ingredients[i]
        else:
            raise ValueError("Some ingredients are unavailable", unavailable_ingredients)
        return needed_ingredients