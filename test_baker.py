import pytest
from  baker import Bakery

# STEP 1: write the production code to ensure the test passes. 

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
