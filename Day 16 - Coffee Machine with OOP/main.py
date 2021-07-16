from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to have? ({options}) ").lower()
    if choice == "report":
        report = coffee_machine.report()
        print(report)
    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(choice)
        print(drink)
        if coffee_machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
