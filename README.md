# 👨🏽‍🍳 Pizza Builder 🍕

<br>

**This application allows a user to decorate their pizza using the decorator pattern.**

<br>

The two modules for this assignment are:

1. `python_pizza`

2. `user_interface_pizza`

<br>

**To execute the program, user must run the `python_pizza.py` module where the `main()` function is located.**

<br>

Every customer(the user) starts with the `signature crust` at the low cost of `$4.99` , each time getting prompted on what type of ingredients/toppings they want to add such as the type of:

- **Cheese**
  - MozzarellaCheese - $1.00
  - Cheddar - $1.00
  - Provolone - $1.50
  - Gouda - $1.75
- **Meat**
  - Pepperoni - $2.00
  - Ham - $2.30
  - Bacon - $2.75
  - Salami - $2.00
  - Sausage - $1.75
- **Vegetables**
  - GreenPepper - $1.00
  - Mushroom - $1.25
  - Onion - $1.00
  - Spinach - $1.40

<br>

The `BasePizza class` and the `PizzaBuilder class` both implement the `AbstractPizza class`. The PizzaBuilder is the decorator which decorates the BasePizza with different types of Topping Decorators as mentioned above.

<br>

The `UserInterface class` located in the `user_interface_pizza.py` module implements all the necessary prompts of the options the user may choose to select. It also contains the `checkout` function which displays the receipt to the user along with each selected topping and its corresponding prices and the grand total.

<br>

## modules and classes:

- **python_pizza.py**

  - ```python
    class AbstractPizza
    class PizzaBuilder
    class BasePizza
    # cheese types
    class MozzarellaCheese
    class Cheddar
    class Provolone
    class Gouda
    # meat types
    class Pepperoni
    class Ham
    class Bacon
    class Salami
    class Sausage
    # veggie types
    class GreenPepper
    class Mushroom
    class Onion
    class Spinach
    
    # contains the dictionary for each topping type
    class Toppings
    ```
  <br>

- **user_interface_pizza.py**

  - `class UserInterface`
