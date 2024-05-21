def cake(ingredients, recipe):
    for elt in recipe:
        if ingredients.get(elt):
            return ingredients.get(elt)//recipe.get(elt)
    return 0