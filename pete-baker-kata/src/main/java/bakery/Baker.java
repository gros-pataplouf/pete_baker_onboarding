package bakery;
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
        int quantity = 0;
        for (String ingredient: recipe.keySet()) {
            quantity = available.getOrDefault(ingredient, 0) / recipe.get(ingredient);
        }
        return quantity;


    }
}
