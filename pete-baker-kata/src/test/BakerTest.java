package main;

import java.util.HashMap;
import static org.junit.Assert.assertTrue;
import org.junit.Test;

/**
 * Unit test for simple App.
 */
public class BakerTest
{

    @Test
    public void cakeTestReturns1()
    {
        HashMap<String, Integer> recipe = new HashMap<>();
        recipe.put("flour", 200);
        HashMap<String, Integer> available = new HashMap<>();
        available.put("flour", 200);
        int numOfCakes = Baker.cakes(available, recipe);
        assertTrue(numOfCakes == 1);
    }
    @Test
    public void returns0IfIngredientUnavailable() {
        HashMap<String, Integer> recipe = new HashMap<>();
        recipe.put("flour", 200);
        HashMap<String, Integer> available = new HashMap<>();
        int numOfCakes = Baker.cakes(available, recipe);
        assertTrue(numOfCakes == 0);

    }
    @Test
    public void worksForSeveralIngredients() {
        HashMap<String, Integer> recipe = new HashMap<>();
        recipe.put("flour", 200);
        recipe.put("sugar", 200);
        recipe.put("butter", 100);
        recipe.put("vanilla extract", 2);
        recipe.put("kefir", 400);
        recipe.put("apples", 3);
        HashMap<String, Integer> available = new HashMap<>();
        available.put("flour", 1000);
        available.put("sugar", 500);
        available.put("butter", 250);
        available.put("vanilla extract", 20);
        available.put("kefir", 900);
        available.put("apples", 9);
        int numOfCakes = Baker.cakes(available, recipe);
        assertTrue(numOfCakes == 2);

    }

}
