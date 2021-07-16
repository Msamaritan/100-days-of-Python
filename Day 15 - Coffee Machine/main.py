# one penny --> 0.01
# one nickel --> 0.05
# one dime --> 0.10
# one quarter --> 0.25

from resources import MENU, resources


def check_resource(drink_ingredients):
    """Checks whether the ingredients in the machine enough to make the drink"""
    for items in resources:
        if drink_ingredients[items] > resources[items]:
            print(f"Sorry there's not enough {items}!")
            return False
    return True


def is_transaction(amt, drink_amt):
    """Checks whether the user inputs enough money and if extra money, it returns the change"""
    if amt >= drink_amt:
        change = round(amt - drink_amt, 2)
        print(f"The change is {change}")
        global profit
        profit += drink_amt
        return True
    return False


def make_coffee(drink_ingredients):
    """Deducts the ingredients spend on this transaction from the resources"""
    for item in resources:
        resources[item] -= drink_ingredients[item]
    print("Enjoy your Coffee!")


is_on = True
profit = 0

while is_on:
    response = input("What would you like to have? Latte/Cappuccino/espresso: ").lower()
    if response == "off":
        print("Machine turned off")
        is_on = False

    elif response == "report":
        for key in resources:
            print(f"{key} = {resources[key]}")
        print(f"Profit = {profit}")

    else:
        coffee = MENU[response]

        if check_resource(coffee["ingredients"]):
            print("Please insert coins.")
            penny = float(input("How many pennies? ")) * 0.01
            nickel = float(input("How many nickels? ")) * 0.05
            dime = float(input("How many dimes? ")) * 0.10
            quarter = float(input("How many quarter? ")) * 0.25
            amount = penny + nickel + dime + quarter
            if is_transaction(amount, coffee["cost"]):
                make_coffee(coffee["ingredients"])

        else:
            is_on = False








