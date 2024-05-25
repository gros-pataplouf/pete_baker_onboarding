def cake(*args):
    if len(args) != 2:
        raise Exception("This function takes exactely two arguments")
    for arg in args:
        if not isinstance(arg, dict):
            raise ValueError("Arguments must be dictionaries.")
    recipe, available = args
    recipe_items = set(recipe.items())
    available_items = set(available.items())
    if not recipe_items.issubset(available_items):
        return 0
