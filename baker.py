def cake(available, recipe):
    max_cakes = 0
    for ingredient in recipe:
        if ingredient in available:
            available_quantity = available[ingredient]
            required_quantity = recipe[ingredient]
            ingredient_quotient = available[ingredient]//recipe[ingredient]
            if available_quantity < required_quantity:
                return 0
            if max_cakes == 0 or max_cakes > ingredient_quotient:
                max_cakes = ingredient_quotient
        else:
            return 0
    return max_cakes