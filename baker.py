def cake(*args):
    if len(args) != 2:
        raise Exception("This function takes exactely two arguments")
    for arg in args:
        if not isinstance(arg, dict):
            raise ValueError("Arguments must be dictionaries.")
    recipe, available = args
    max_cakes = 0
    return max_cakes