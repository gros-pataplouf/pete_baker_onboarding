import pytest
from  baker import Bakery

# STEP 1: write the production code to ensure the test passes. 

def test_bakery_has_name():
    petes_bakery = Bakery("Sweet Pete")
    assert petes_bakery.name == "Sweet Pete"

