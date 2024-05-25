def cake(*args):
    if len(args) != 2:
        raise Exception("This function takes exactely two arguments")
    for arg in args:
        if not isinstance(arg, dict):
            raise TypeError("Arguments must be dictionaries.")
    available, recipe  = args
    recipe_ingredients = set(recipe.keys())
    available_ingredients = set(available.keys())
    if not recipe_ingredients.issubset(available_ingredients):
        return 0
    return min([available[ingredient] // recipe[ingredient] for ingredient in recipe_ingredients])