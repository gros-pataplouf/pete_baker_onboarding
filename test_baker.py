from  baker import cake

# case 1: one ingredient cake, recipe only for one ingredient same quantity
# case 2: one ingredient cake, recipe only for one ingredient same quantity, division result is float < 0
# case 3: one ingredient cake, recipe only another ingredient
# case 4: cake with several available, recipe with several available, partial overlap, cake not possible
# case 5: cake with several available, recipe with several, recipe is subs. of available, cake possible


def test_cake_only_one_ingredient():
    available = {"flour": 500}
    recipe = {"flour": 500}
    result = cake(available, recipe)
    assert result == 1

def test_one_ingredient_not_in_recipe():
    available = {"flour": 500}
    recipe = {"milk": 500}
    result = cake(available, recipe)
    assert result == 0

def test_returns_0_if_ingredient_insufficient():
    available = {"sugar": 500}
    recipe = {"sugar": 600}
    result = cake(available, recipe)
    assert result == 0

def test_returns_num_of_cakes_if_all_available_enough():
    available = {"sugar": 500, "milk": 250, "flour": 700, "eggs": 12}
    recipe = {"sugar": 100, "milk": 100, "flour": 340, "eggs": 1}
    result = cake(available, recipe)
    assert result == 2

def test_returns_0_if_one_ingredient_not_enough():
    available = {"sugar": 500, "milk": 30, "flour": 700, "eggs": 12}
    recipe = {"sugar": 100, "milk": 100, "flour": 340, "eggs": 1}
    result = cake(available, recipe)
    assert result == 0

def test_returns_0_if_one_ingredient_missing():
    available = {"sugar": 500, "flour": 700, "eggs": 12}
    recipe = {"sugar": 100, "milk": 100, "flour": 340, "eggs": 1}
    result = cake(available, recipe)
    assert result == 0



    
