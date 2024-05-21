from  baker import cake

# case 1: one ingredient cake, recipe only for one ingredient same quantity
# case 2: one ingredient cake, recipe only for one ingredient same quantity, division result is float < 0
# case 3: one ingredient cake, recipe only another ingredient
# case 4: cake with several ingredients, recipe with several ingredients, partial overlap, cake not possible
# case 5: cake with several ingredients, recipe with several, recipe is subs. of ingredients, cake possible


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

def test_returns_0_if_ingredient_insufficient():
    ingredients = {"sugar": 500}
    recipe = {"sugar": 600}
    result = cake(ingredients, recipe)
    assert result == 0

def test_returns_num_of_cakes_if_all_ingredients_enough():
    ingredients = {"sugar": 500, "milk": 250, "flour": 700, "eggs": 12}
    recipe = {"sugar": 100, "milk": 100, "flour": 340, "eggs": 1}
    result = cake(ingredients, recipe)
    assert result == 2

    
