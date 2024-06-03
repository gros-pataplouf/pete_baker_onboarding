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