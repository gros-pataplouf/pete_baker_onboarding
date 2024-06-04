import json

class Recipe:

    def __init__(self, name : str, ingredients : dict):
        self.__name = name
        self.__ingredients = ingredients

    @property
    def name(self):
        return self.__name
    
    @property
    def ingredients(self):
        return self.__ingredients
    

class Bakery:
    
    def __init__(self, name : str):
        self.__name = name
        self.__pantry = {}
        self.recipes = [Recipe(**description) for description in self.get_recipes()]

    def __add__(self, ingredients : dict) -> object:
        for i in ingredients:
            self.__pantry[i] = self.__pantry.get(i, 0) + ingredients[i]
        return self
    
    def get_recipes(self) -> list:
        with open("recipes.json") as recipe_file:
            recipes = json.load(recipe_file)
        return recipes

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def pantry(self) -> dict:
        return self.__pantry

    def use(self, needed_ingredients : dict) -> dict :
        unavailable_ingredients = list(filter(lambda ingredient: self.__pantry[ingredient] <= needed_ingredients[ingredient], needed_ingredients))
        if not unavailable_ingredients:
            for i in needed_ingredients:
                self.__pantry[i] -= needed_ingredients[i]
        else:
            raise ValueError("Some ingredients are not available in sufficient quantity, please check the pantry.", unavailable_ingredients)
        return needed_ingredients
    
    def get_ingredients(self, recipe_name : str) -> dict :
        for recipe in self.recipes:
            print(recipe.name, recipe_name)
            if recipe.name == recipe_name:
                print(recipe.ingredients)
                return recipe.ingredients
