import pytest
from  baker import cake

#STEP 1: Adapt the production code to make to first test pass.

def test_cake_only_one_ingredient():
    available = {"flour": 500}
    recipe = {"flour": 500}
    result = cake(available, recipe)
    assert result == 1

#STEP 2: Delete the @pytest.mark.skip decorator for each of these tests and adapt the production code to make tests pass.

@pytest.mark.skip
def test_one_ingredient_not_in_recipe():
    available = {"flour": 500}
    recipe = {"milk": 500}
    result = cake(available, recipe)
    assert result == 0

@pytest.mark.skip
def test_returns_0_if_ingredient_insufficient():
    available = {"sugar": 500}
    recipe = {"sugar": 600}
    result = cake(available, recipe)
    assert result == 0

# STEP 3: now write a test for the following case: cake function should return a positive integer if all ingredients are available in sufficient quantity

# STEP 4: now write a test for the following case: cake function should return 0 if at least one ingredient is available in insufficient quantity

# STEP 5: one scenario has not been considered. Can you figure out which one it is, and cover the edge case?
