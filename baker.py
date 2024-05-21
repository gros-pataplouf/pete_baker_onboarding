def cake(ingredients, recipe):
    max_cakes = 0
    for elt in recipe:
        if ingredients.get(elt):
            ingredient_quotient = ingredients.get(elt)//recipe.get(elt)
            if max_cakes == 0 or max_cakes > ingredient_quotient:
                max_cakes = ingredient_quotient


    return max_cakes