import pytest
from  baker import cake

# tests: takes two objects / dictionaires
# unavailable ingredient considered a 0
# returns zero if at least one ingredient in insufficient quantity 
# throws if 
# wrong number of arguments 

"""
Can you help him to find out, how many cakes he could bake considering his recipes?
Write a function cakes(), which takes the recipe (object) and the available ingredients(also an object)
and returns the maximum number of cakes Pete can bake (integer).
For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).
Ingredients that are not present in the objects, can be considered as 0.
Examples: // must return 2 cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200}); // must return 0 cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000});
"""

def test_cake_takes_two_args():
    cake({"flour": 400}, {"milk": 200})
    assert True

def test_throws_if_args_not_dicts():
    with pytest.raises(TypeError) as e:
        cake("foo", 123)
    assert str(e.value) == "Arguments must be dictionaries."

def test_returns_0_if_one_ingredient_missing():
    available = {"sugar": 500, "flour": 700, "eggs": 12}
    recipe = {"sugar": 100, "milk": 100, "flour": 340, "eggs": 1}
    result = cake(available, recipe)
    assert result == 0

def test_returns_3_if_triple_of_recipe():
    available = {"apples": 3}
    recipe = {"apples" : 1}
    assert cake(available, recipe) == 3

def test_returns_0_if_ingredient_insufficient():
    available = {"sugar": 500}
    recipe = {"sugar": 600}
    result = cake(available, recipe)
    assert result == 0

def test_returns_num_of_cakes_for_several_ingredients():
    available = {"sugar": 500, "milk": 250, "flour": 700, "eggs": 12}
    recipe = {"sugar": 100, "milk": 100, "flour": 70, "eggs": 1}
    result = cake(available, recipe)
    assert result == 2

def test_ingredient_order_does_not_matter():
    available = {"sugar": 500, "milk": 250, "flour": 700, "eggs": 12}
    recipe = {"milk": 100, "eggs": 1, "flour": 70, "sugar": 100}
    result = cake(available, recipe)
    assert result == 2


