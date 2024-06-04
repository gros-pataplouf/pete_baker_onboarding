import pytest, json
from  baker import Bakery, Recipe


def test_bakery_has_name():
    petes_bakery = Bakery("Sweet Pete")
    assert petes_bakery.name == "Sweet Pete"

def test_name_cannot_be_changed_from_outside():
    petes_bakery = Bakery("Pete's Delights")
    with pytest.raises(Exception):
        petes_bakery.name = "Flour Power"
    assert petes_bakery.name == "Pete's Delights"
    
def test_starts_out_with_empty_pantry():
    petes_bakery = Bakery("Pete's Delights")
    assert petes_bakery.pantry == {}

def test_can_stock_pantry():
    petes_bakery = Bakery("Pete's Delights")
    petes_bakery += {"sugar": 500, "butter": 200}
    assert petes_bakery.pantry == {"sugar": 500, "butter": 200}

def test_can_increment_existing_ingredient_quantity():
    petes_bakery = Bakery("Pete's Delights")
    petes_bakery += {"sugar": 500, "butter": 200}
    petes_bakery += {"sugar": 500, "butter": 200}
    assert petes_bakery.pantry == {"sugar": 1000, "butter": 400}

def test_if_ingredient_available_returns_needed_quantity():
    petes_bakery = Bakery("Pete's Delights")
    petes_bakery += {"sugar": 500, "butter": 200}
    needed_ingredient = petes_bakery.use({"sugar": 100})
    assert needed_ingredient == {"sugar": 100}

def test_pantry_diminishes_if_ingredient_used():
    petes_bakery = Bakery("Pete's Delights")
    petes_bakery += {"sugar": 500, "butter": 200}
    petes_bakery.use({"sugar": 100})
    assert petes_bakery.pantry == {"sugar": 400, "butter": 200}

def test_throws_if_ingredient_insufficient_and_puts_back_on_shelf():
    petes_bakery = Bakery("Pete's Delights")
    petes_bakery += {"sugar": 500, "butter": 200}
    with pytest.raises(ValueError):
        petes_bakery.use({"sugar": 600, "butter": 50})
    assert petes_bakery.pantry == {"sugar": 500, "butter": 200}

def test_recipe_has_name_and_recipe():
    recipe = Recipe("Lemon pie", {"lemons": 3, "eggs": 3, "flour": 200, "sugar": 150, "butter": 150})
    assert recipe.name == "Lemon pie"
    assert recipe.ingredients.get("lemons") == 3

def test_bakery_has_recipes():
    petes_bakery = Bakery("Pete's Delights")
    assert len(petes_bakery.recipes) == 5
    assert isinstance(petes_bakery.recipes[0], Recipe)

def test_can_get_ingredients_by_recipe_name():
    petes_bakery = Bakery("Pete's Delights")
    for recipe in petes_bakery.recipes:
        print(recipe)
    lemon_pie_ingredients = petes_bakery.get_ingredients("Lemon Pie")
    assert lemon_pie_ingredients == { "butter": 100, "eggs": 3, "flour": 200,  "lemons": 3, "sugar": 150 }



# def test_max_cakes_takes_two_args():
#     try:
#         cake({"flour": 400}, {"milk": 200})
#     except Exception:
#         assert False

# def test_throws_if_args_not_dicts():
#     with pytest.raises(TypeError) as e:
#         cake("foo", 123)
#     assert str(e.value) == "Arguments must be dictionaries."

# def test_returns_0_if_one_ingredient_missing():
#     available = {"sugar": 500, "flour": 700, "eggs": 12}
#     recipe = {"sugar": 100, "milk": 100, "flour": 340, "eggs": 1}
#     result = cake(available, recipe)
#     assert result == 0

# def test_returns_3_if_triple_of_recipe():
#     available = {"apples": 3}
#     recipe = {"apples" : 1}
#     assert cake(available, recipe) == 3

# def test_returns_0_if_ingredient_insufficient():
#     available = {"sugar": 500}
#     recipe = {"sugar": 600}
#     result = cake(available, recipe)
#     assert result == 0

# def test_returns_num_of_cakes_for_several_ingredients():
#     available = {"sugar": 500, "milk": 250, "flour": 700, "eggs": 12}
#     recipe = {"sugar": 100, "milk": 100, "flour": 70, "eggs": 1}
#     result = cake(available, recipe)
#     assert result == 2

# def test_ingredient_order_does_not_matter():
#     available = {"sugar": 500, "milk": 250, "flour": 700, "eggs": 12}
#     recipe = {"milk": 100, "eggs": 1, "flour": 70, "sugar": 100}
#     result = cake(available, recipe)
#     assert result == 2

