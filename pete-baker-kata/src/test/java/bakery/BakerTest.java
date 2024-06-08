package bakery;

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
        Baker pete = new Baker();
        int numOfCakes = pete.cakes(available, recipe);
        assertTrue(numOfCakes == 1);
    }
    @Test
    public void returns0IfIngredientUnavailable() {
        HashMap<String, Integer> recipe = new HashMap<>();
        recipe.put("flour", 200);
        HashMap<String, Integer> available = new HashMap<>();
        Baker pete = new Baker();
        int numOfCakes = pete.cakes(available, recipe);
        assertTrue(numOfCakes == 0);

    }
}
