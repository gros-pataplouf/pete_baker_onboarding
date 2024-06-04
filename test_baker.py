import pytest, json
from  baker import Bakery, Recipe


@pytest.fixture
def setup_recipe_list():
    with open("recipes.json") as recipe_file:
        recipes = json.load(recipe_file)
    return recipes 

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

def test_recipe_has_name_and_ingredients():
    recipe = Recipe("Lemon pie", {"lemons": 3, "eggs": 3, "flour": 200, "sugar": 150, "butter": 150})
    assert recipe.name == "Lemon pie"
    assert recipe.ingredients.get("lemons") == 3

def test_bakery_has_recipes():
    petes_bakery = Bakery("Pete's Delights")
    assert len(petes_bakery.recipes) == 5
    assert isinstance(petes_bakery.recipes[0], Recipe)

def test_can_get_ingredients_by_recipe_name(setup_recipe_list):
    petes_bakery = Bakery("Pete's Delights")
    petes_bakery.recipes = setup_recipe_list
    lemon_pie_ingredients = petes_bakery.get_ingredients_by_recipe_name("Lemon Pie")
    assert lemon_pie_ingredients == { "butter": 100, "eggs": 3, "flour": 200,  "lemons": 3, "sugar": 150 }


def test_max_cakes_takes_two_args():
    petes_bakery = Bakery("Pete's Delights")
    petes_bakery += {"flour": 1000, "cocoa powder": 500}
    try:
        petes_bakery.max_cakes("Lemon Pie")
    except Exception:
        assert False

def test_max_cakes_0_if_at_least_one_ingredient_missing():
    petes_bakery = Bakery("Pete's Delights")
    petes_bakery += {"flour": 1000, "cocoa powder": 500}
    result = petes_bakery.max_cakes("Lemon Pie")
    assert result == 0

def test_returns_3_if_triple_of_recipe():
    petes_bakery = Bakery("Pete's Delights")
    petes_bakery += {"flour": 1000, "cocoa powder": 500, "apples": 9}
    applecake_recipe = Recipe("Apple Cake", {"apples": 3})
    petes_bakery.recipes.append(applecake_recipe)
    result = petes_bakery.max_cakes("Apple Cake")
    assert result == 3

def test_rounds_down_to_least_available_ingredient():
    petes_bakery = Bakery("Pete's Delights")
    petes_bakery += {"flour": 1000, "cocoa powder": 500, "apples": 9, "flour": 900, "butter": 400}
    applecake_recipe = Recipe("Apple Cake", {"apples": 3, "flour": 300, "butter": 400})
    petes_bakery.recipes.append(applecake_recipe)
    result = petes_bakery.max_cakes("Apple Cake")
    assert result == 1


