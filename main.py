MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = round(quarters + dimes + nickles + pennies, 2)
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
    return True

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("The machine is shutting down...")
        machine_on = False
    elif choice == "report":
        for resource, amount in resources.items():
            unit = "ml" if resource != "coffee" else "g"
            print(f"{resource.capitalize()}: {amount}{unit}")
        print(f"Money: ${money}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                money += drink["cost"]
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid selection. Please choose espresso, latte, cappuccino, report, or off.")
