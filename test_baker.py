from  baker import cake

# case 1: one ingredient cake, recipe only for one ingredient same quantity
# case 1a: one ingredient cake, recipe only for one ingredient same quantity, division result is float > 0
# case 1b: one ingredient cake, recipe only for one ingredient same quantity, division result is float > 0
# case 2: one ingredient cake, recipe only another ingredient
# case 3: cake with several ingredients, recipe with several ingredients, partial overlap, cake not possible
# case 4: cake with several ingredients, recipe with several, recipe is subs. of ingredients, cake possible


def test_cake_only_one_ingredient():
    ingredients = {"flour": 500}
    recipe = {"flour": 500}
    result = cake(ingredients, recipe)
    assert result == 1

def test_one_ingredient_not_in_recipe():
    ingredients = {"flour": 500}
    recipe = {"milk": 500}
    result = cake(ingredients, recipe)
    assert result == 0
