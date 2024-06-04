# An introduction to TDD based on the Kata "Pete, the baker"

## 1. The Kata "Pete the Baker"

Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths.

Can you help him to find out, how many cakes he could bake considering his recipes?

### Recipes and Ingredients. 

#### 1.The Bakery.
- Model the bakery as a class. Pete's Bakery has a name.    
- The bakery has a pantry of available ingredients, which is a dictionary. 
- The baker can add ingredients to stock the pantry.
- The baker can use ingredients from the pantry.
- If the baker tries to use of an ingredient than what is available, the application throws an error. Any ingredients taken before are then restored to the pantry. 



#### 2. The Recipes.
- The bakery has a list of recipes, which is created when the bakery is instantiated.
- A recipe is has a name, as well as a list of ingredients associated with it. 
- You can look up the ingredients by searching for the name of the recipe. 
- Write a function max_cakes(), which takes the recipe name, and the ingredients available in the pantry and returns the maximum number of cakes Pete can bake (integer).




#### 3. The customers: 
- a customer is a person, who has a name
- a customer has a wallet, which 
- can buy a cake from the bakery if it is on display
- ensure the customers cannot change the bakery's name. 
- can place an Order. 
- the bakery can accept or refuse the order, depending on whether the ingredients 
- 




Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer).

For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

_Examples:_
- must return 2:
 `cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})` 
- must return 0:
  `cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})`

Original link [Be careful not to review answers until you’ve completed your answer] https://www.codewars.com/kata/525c65e51bf619685c000059

## 2. Solving the kata with TDD

### a) Setting up the repository
[The following tasks should be done by only one group member.]
- Create a new repository within the organization (TechRisersWomenGroupCodingSessions)[https://github.com/TechRisersWomenGroupCodingSessions].
- Clone the branch required for your language by running `git clone -b <branchname> --single-branch <remote-repo-url>`. <branchname> can be python, javascript or java. // Those branches are not set up yet.     
- Rename the branch to main. `git branch -m main`.
- Change the remote repository to your own (instead of the one you cloned) `git remote set-url origin <YOUR_NEW_REPO>`
- Set your own repo as upstream by pushing local content to the new remote `git push -u origin main`. 
[Task for the other group members]
- Now the other group members can clone your new repo to their local machines.

### b) Setting up the environment
_to be completed with instructions specific for each programming language. e.g. pipenv for python `pip install`, `pipenv shell`, `pip install -r requirements.txt`, but there are many others..._

### c) Getting started.
Have a look at the material:
- baker.py (adjust filename for javascript and java branch) will contain the production code. Currently, it only contains a function cake() which does not return anything. 
-  test_baker.py (adjust filename for javascript and java branch) contains the test. There are already some prewritten tests and steps outlined to get you started. 


