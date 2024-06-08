package main;
import java.util.HashMap;


/**
 * Hello world!
 *
 */
public class Baker 
{
    public static void main( String[] args )
    {
        System.out.println( "Welcome to Pete's Bakery!" );
    }
    public static int cakes(HashMap<String, Integer> available, HashMap<String, Integer> recipe) {
        int cakeCounter = 0;
        int loopCounter = 0;
        for (String ingredient: recipe.keySet()) {
            int ratioForIngredient = available.getOrDefault(ingredient, 0) / recipe.get(ingredient);
            if (loopCounter == 0) {
                cakeCounter = ratioForIngredient;
            } else {
                if (ratioForIngredient < cakeCounter) {
                    cakeCounter = ratioForIngredient;
                }
            }
            loopCounter++;
        }
        return cakeCounter;
    }
}
