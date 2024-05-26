def cake(available: object, recipe: object) -> int:
    for arg in [available, recipe]:
        if not isinstance(arg, dict):
            raise TypeError("Arguments must be dictionaries.")
    return min([available.get(ingredient, 0) // recipe[ingredient] for ingredient in recipe.keys()])