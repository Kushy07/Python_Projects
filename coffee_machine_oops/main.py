from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_menu = Menu()

types = my_menu.get_items()
my_coffeemaker = CoffeeMaker()
my_moneymachine = MoneyMachine()

switch_off = False

while not switch_off:

    user = input(f"What would you like? ({types}) ").lower()

    if user == 'report':
        my_coffeemaker.report()
        my_moneymachine.report()
    elif user == 'off':
        switch_off = True
    else:
        my_menu_item = my_menu.find_drink(user)
        if my_coffeemaker.is_resource_sufficient(my_menu_item) and my_moneymachine.make_payment(my_menu_item.cost):
            my_coffeemaker.make_coffee(my_menu_item)




