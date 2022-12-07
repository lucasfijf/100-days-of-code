from data import MENU, resources

def report_resources(resources, money):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"

def sufficient_resources(ingredients):
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return total

def prepare_coffee(coffee_type, coffee, ingredients, coins):
    for ingredient in ingredients:
        resources[ingredient] -= coffee["ingredients"][ingredient]
    print(f"Here is your {coffee_type} ☕ Enjoy!")

def coffee_machine():
    money = 0
    should_continue = True
    while should_continue:
        prompt = input("What would you like? (expresso/latte/cappuccino): ").lower()
        if prompt == "off":
            should_continue = False
        elif prompt == "report":
            report = report_resources(resources, money)
            print(report)
        else:
            coffee = MENU[prompt]
            ingredients = coffee["ingredients"]
            check = sufficient_resources(ingredients)
            if check is True:
                coins = process_coins()
                if coins < coffee["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                elif coins == coffee["cost"]:
                    money += coins
                    prepare_coffee(prompt, coffee, ingredients, coins)
                elif coins > coffee["cost"]:
                    change = coins - coffee["cost"]
                    money += coins - change
                    print(f"Here is ${change} dollars in change.")
                    prepare_coffee(prompt, coffee, ingredients, change)

coffee_machine()