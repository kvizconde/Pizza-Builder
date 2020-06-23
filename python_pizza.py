import abc

from user_interface_pizza import *

"""
This module contains all the classes that are needed to assemble a pizza:
AbstractPizza class
BasePizza class which implements AbstractPizza
PizzaBuilder class which implements AbstractPizza
Different class toppings such as cheese toppings, meat toppings, veggie toppings.
"""


class AbstractPizza(abc.ABC):
    """
    This is the Abstract Pizza class which gets implemented by
    the BasePizza and the PizzaBuilder Decorator
    """

    @abc.abstractmethod
    def get_ingredients(self):
        pass

    @abc.abstractmethod
    def get_price(self):
        pass

    @abc.abstractmethod
    def assemble_pizza(self):
        pass


class PizzaBuilder(AbstractPizza):
    """
    This class implements the AbstractPizza class and acts as the Decorator
    to decorate the BasePizza class
    """

    def __init__(self, decorated_pizza):
        self.decorated_pizza = decorated_pizza
        self.ingredient_list = decorated_pizza.ingredient_list

    def get_ingredients(self):
        return self.decorated_pizza.get_ingredients()

    def get_price(self):
        return self.decorated_pizza.get_price()

    def assemble_pizza(self):
        self.ingredient_list.append(self.get_ingredients())
        return '\n+ '.join(
            self.decorated_pizza.ingredient_list) + f"\nCost: ${'%.2f' % self.get_price()}"

    def __str__(self):
        return f"\n{self.assemble_pizza().title()}"


class BasePizza(AbstractPizza):
    """
    This class implements the AbstractPizza class and acts as the 'Wrappee'
    which gets wrapped by the PizzaBuilder decorator
    """

    def __init__(self):
        self.ingredient_list = []

    def get_ingredients(self):
        """
        All pizza starts with the signature crust
        :return: the signature crust, a mandatory ingredient
        """
        return "signature crust"

    def get_price(self):
        """
        The starting price of all pizza
        :return: 4.99 the price in CAD
        """
        return 4.99

    def assemble_pizza(self):
        """
        This method handles the new ingredients being added into the ingredient list
        :return: a String of the current ingredient list
        """
        self.ingredient_list.append(self.get_ingredients())
        return '\n'.join(self.ingredient_list)

    def __str__(self):
        """
        The toString method returns the assemble_pizza function and the cost
        :return: assemble_pizza and the price
        """
        return f"{self.assemble_pizza().title()} \nCost: ${self.get_price()}"


# Concrete Cheese Type Classes, extends the Decorator class
class MozzarellaCheese(PizzaBuilder):
    def __init__(self, decorated_pizza):
        super(MozzarellaCheese, self).__init__(decorated_pizza)
        self.decorated_pizza = decorated_pizza

    def get_ingredients(self):
        return "mozzarella"

    def get_price(self):
        return super(MozzarellaCheese, self).get_price() + 1


class Cheddar(PizzaBuilder):
    def __init__(self, decorated_pizza):
        super(Cheddar, self).__init__(decorated_pizza)
        self.decorated_pizza = decorated_pizza

    def get_ingredients(self):
        return "cheddar"

    def get_price(self):
        return super().get_price() + 1


class Provolone(PizzaBuilder):
    def __init__(self, decorated_pizza):
        super(Provolone, self).__init__(decorated_pizza)
        self.decorated_pizza = decorated_pizza

    def get_ingredients(self):
        return "provolone"

    def get_price(self):
        return super(Provolone, self).get_price() + 1.50


class Gouda(PizzaBuilder):
    def __init__(self, decorated_pizza):
        super(Gouda, self).__init__(decorated_pizza)
        self.decorated_pizza = decorated_pizza

    def get_ingredients(self):
        return "gouda"

    def get_price(self):
        return super().get_price() + 1.75


# Concrete Meat Type Classes, extends the Decorator class
class Pepperoni(PizzaBuilder):
    def __init__(self, decorated_pizza):
        super(Pepperoni, self).__init__(decorated_pizza)
        self.decorated_pizza = decorated_pizza

    def get_ingredients(self):
        return "pepperoni"

    def get_price(self):
        return super().get_price() + 2


class Ham(PizzaBuilder):
    def __init__(self, decorated_pizza):
        super(Ham, self).__init__(decorated_pizza)
        self.decorated_pizza = decorated_pizza

    def get_ingredients(self):
        return "ham"

    def get_price(self):
        return super().get_price() + 2.30


class Bacon(PizzaBuilder):
    def __init__(self, decorated_pizza):
        super(Bacon, self).__init__(decorated_pizza)
        self.decorated_pizza = decorated_pizza

    def get_ingredients(self):
        return "bacon"

    def get_price(self):
        return super().get_price() + 2.75


class Salami(PizzaBuilder):
    def __init__(self, decorated_pizza):
        super(Salami, self).__init__(decorated_pizza)
        self.decorated_pizza = decorated_pizza

    def get_ingredients(self):
        return "salami"

    def get_price(self):
        return super().get_price() + 2


class Sausage(PizzaBuilder):
    def __init__(self, decorated_pizza):
        super(Sausage, self).__init__(decorated_pizza)
        self.decorated_pizza = decorated_pizza

    def get_ingredients(self):
        return "sausage"

    def get_price(self):
        return super().get_price() + 1.75


# Concrete Vegetable Type Classes, extends the Decorator class
class GreenPepper(PizzaBuilder):
    def __init__(self, decorated_pizza):
        super(GreenPepper, self).__init__(decorated_pizza)
        self.decorated_pizza = decorated_pizza

    def get_ingredients(self):
        return "green peppers"

    def get_price(self):
        return super().get_price() + 1


class Mushroom(PizzaBuilder):
    def __init__(self, decorated_pizza):
        super(Mushroom, self).__init__(decorated_pizza)
        self.decorated_pizza = decorated_pizza

    def get_ingredients(self):
        return "mushrooms"

    def get_price(self):
        return super().get_price() + 1.25


class Onion(PizzaBuilder):
    def __init__(self, decorated_pizza):
        super(Onion, self).__init__(decorated_pizza)
        self.decorated_pizza = decorated_pizza

    def get_ingredients(self):
        return "onions"

    def get_price(self):
        return super().get_price() + 1


class Spinach(PizzaBuilder):
    def __init__(self, decorated_pizza):
        super(Spinach, self).__init__(decorated_pizza)
        self.decorated_pizza = decorated_pizza

    def get_ingredients(self):
        return "spinach"

    def get_price(self):
        return super().get_price() + 1.4


class Toppings:
    """
    This class holds the dictionary for each type of cheese, meat, veggies
    """
    cheese_dict = {1: MozzarellaCheese, 2: Cheddar, 3: Provolone,
                   4: Gouda}
    meat_dict = {1: Pepperoni, 2: Ham, 3: Bacon, 4: Salami,
                 5: Sausage}
    veggie_dict = {1: GreenPepper, 2: Mushroom, 3: Onion, 4: Spinach}


def main():
    ui = UserInterface()
    ui.main_menu()


if __name__ == '__main__':
    main()
