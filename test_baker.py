import pytest
from  baker import cake


def test_cake_takes_two_args():
    try:
        cake({"flour": 400}, {"milk": 200})
    except Exception:
        assert False

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


