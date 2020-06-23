import random
import time

from python_pizza import BasePizza, Toppings

"""
This module contains one class: UserInterface
The UserInterface class handles all the user interaction which allow the user
to build amazing pizza.
"""


class UserInterface:
    """
    This class contains all the required methods for user interaction as follows:
    > main_menu
    > topping_menu
    > print_topping_choice
    > checkout
    """

    def main_menu(self):
        """
        This method handles the menu introduction
        and kicks off the first topping_menu which is cheese menu
        """
        my_pizza = BasePizza()
        cheese_selection = Toppings.cheese_dict
        print("\x1b[6;30;43m 👨🏽‍🍳 Welcome to Kevin's Pizzeria! 🍕 \x1b[0m\n")
        print("Lets get you started with the Basics...")
        print(f"\nBasic Pizza: \n{my_pizza}")
        self.topping_menu(my_pizza, cheese_selection, 1)

    def topping_menu(self, my_pizza, topping_choice, next_menu):
        """
        This method handles the menu prompts for each topping type such as cheese, meat and veggie menus

        :param my_pizza: the BasePizza() passed down from the 'main_menu' method
        :param topping_choice: the topping type as a dictionary
        :param next_menu: this number determines which topping menu to display to the user
        :return: recursively returns topping_menu method until each menu has been executed via 'next_menu' condition
        """
        topping = ["", "Cheese", "Protein", "Vegetable", "Pineapple"]
        emoji_topping = ["", "🧀", "🥩", "🍄"]
        chef_names = ["👨🏾‍🍳 Jose", "👨🏽‍🍳 Kevin", "👨🏻‍🍳 Ringo", "👨🏻‍🍳 Benson", "👨🏽‍🍳 Daniel",
                      "👩🏽‍🍳 ‍Rosette", "👩🏻‍🍳 Ashley"]
        msg = ''
        get_topping = 0
        while True:
            if topping_choice == Toppings.cheese_dict:
                msg = f"{emoji_topping[1]} Select your {topping[1]}: "
                get_topping = 1

            elif topping_choice == Toppings.meat_dict:
                msg = f"{emoji_topping[2]} Select your {topping[2]}:"
                get_topping = 2

            elif topping_choice == Toppings.veggie_dict:
                msg = f"{emoji_topping[3]} Select your {topping[3]}:"
                get_topping = 3

            print(f"\n{msg}")
            self.print_topping_choice(get_topping)  # 1: cheese, 2: protein, 3: vegetables
            selection_length = topping_choice
            try:
                user_input = int(input())
                if 0 < user_input <= len(selection_length):
                    my_pizza = topping_choice.get(user_input)(my_pizza)
                    print(
                        f"\n{emoji_topping[get_topping]} Your {topping[get_topping]} "
                        f"Selection: {my_pizza.get_ingredients().title()}")
                    print(f"\n\x1b[0;30;46m 🍕 Your current Pizza: \x1b[0m {my_pizza}")
                    print(f"\nWould you like to add more {topping[get_topping]}? ")
                    print(f"\x1b[0;30;42m 1.Yes \x1b[0m\x1b[0;30;41m 2.Checkout \x1b[0m",
                          f"\n\n\x1b[0;30;43m (Enter any other key for next menu: {topping[get_topping + 1]}) \x1b[0m")
                    prompt_for_more = input()
                    if prompt_for_more == '1':
                        continue
                    elif prompt_for_more == '2':
                        print(f"\n🔥{random.choice(chef_names)} is Firing up your Pizza...")
                        time.sleep(2)  # pause for 2 seconds before displaying receipt to user
                        return self.checkout(my_pizza)
                    else:
                        next_menu += 1
                        break
                else:
                    print(f"\nSorry that {topping[get_topping]} doesn't exist!")
                    print(f"Please select a valid option between 1 and {len(selection_length)}")
                    continue
            except ValueError:
                print("\nDigit only please!")
                print(f"Please select a valid option between 1 and {len(selection_length)}")
                continue

        # The conditions below handle the next topping menu
        if next_menu == 2:
            topping_choice = Toppings.meat_dict
        elif next_menu == 3:
            topping_choice = Toppings.veggie_dict
        elif next_menu == 4:
            # Pineapple Pizza Jokes
            while True:
                try:
                    print("\n🍍 Would you like to add some Pineapple?")
                    print("1.Yes ", "2.No")
                    pineapple_prompt = int(input())
                    if pineapple_prompt == 1:
                        print("\nJust kidding we don't put Pineapple on Pizza! 😂")
                        print(f"\x1b[0;30;42m (Hit any key to Checkout) \x1b[0m")
                        input()
                        print(f"\n🔥{random.choice(chef_names)} is Firing up your Pizza...")
                        time.sleep(2)  # pause for 2 seconds before displaying receipt to user
                        return self.checkout(my_pizza)
                    elif pineapple_prompt == 2:
                        print("\n👍 Good Choice! Who puts Pineapple on Pizza anyways?!")
                        print(f"\x1b[0;30;42m (Hit any key to Checkout) \x1b[0m")
                        input()
                        print(f"\n🔥{random.choice(chef_names)} is Firing up your Pizza...")
                        time.sleep(2)  # pause for 2 seconds before displaying receipt to user
                        return self.checkout(my_pizza)
                    else:
                        print("\nSorry that choice is invalid!, please select only '1' for Yes, '2' for No")
                        continue
                except ValueError:
                    print("\nSorry that choice is invalid!, please select only '1' for Yes, '2' for No")

        # recursively call topping_menu until we reach the end of all menus
        return self.topping_menu(my_pizza, topping_choice, next_menu)

    @staticmethod
    def print_topping_choice(choice):
        """
        This method handles the format for printing the topics and displaying it to the user
        along with the topping price.
        :param choice: the topping choice, 1 for cheese, 2 for meat, 3 for veggie
        """
        my_pizza = BasePizza()
        topping = ''
        if choice == 1:
            topping = Toppings.cheese_dict
        elif choice == 2:
            topping = Toppings.meat_dict
        elif choice == 3:
            topping = Toppings.veggie_dict

        index = 0
        for t in topping:
            index += 1
            print(
                f"{index}. {topping.get(t)(my_pizza).get_ingredients().title()} "
                f"- ${'%.2f' % (topping.get(t)(my_pizza).get_price() - my_pizza.get_price())}")

    @staticmethod
    def checkout(my_pizza):
        """
        The purpose of this function is to handle the receipt and display the user's selected toppings and
        corresponding price along with the total price of their pizza.
        :param my_pizza: the BasePizza wrapped with the latest topping
        :return:
        """
        topping_dict = {1: Toppings.cheese_dict, 2: Toppings.meat_dict, 3: Toppings.veggie_dict}
        pizza = BasePizza()
        price = ['4.99']
        ingredients = [ingredient.title() for ingredient in my_pizza.ingredient_list]

        for k in topping_dict:  # iterates over the topping type dict -> cheese, meat, veggie
            for index in range(len(ingredients)):  # loop through the ingredient list
                for i in topping_dict.get(k):  # loop through each topping class
                    # this condition gets the current topping ingredient to compare with the added ingredient
                    if topping_dict.get(k)[i].get_ingredients(pizza).title() == ingredients[index]:
                        price.append('%.2f' % (topping_dict[k].get(i)(pizza).get_price() - pizza.get_price()))

        ingredients_with_price = ['\n           ↳ $'.join(x) for x in zip(ingredients, price)]

        print("\n\x1b[0;30;46m 👨🏽‍🍳 Your Receipt: \x1b[0m")
        ingredients_with_price.sort()
        ingredients_with_price = '\n--------------------\n'.join(ingredients_with_price)
        total_price = my_pizza.get_price()
        print("--------------------")
        print(f"{ingredients_with_price} "
              f"\n--------------------\n\x1b[0;30;43m 🍕 Total Price: ${'%.2f' % total_price} \x1b[0m")
        exit()
