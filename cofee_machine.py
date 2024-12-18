resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

menu = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
}


def check_resources(drink):
    """Checks if there are enough resources to make the drink."""
    for item in menu[drink]["ingredients"]:
        if menu[drink]["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_payment(cost):
    """Processes the user's payment."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? (0.25): "))
    dimes = int(input("How many dimes? (0.10): "))
    nickels = int(input("How many nickels? (0.05): "))
    pennies = int(input("How many pennies? (0.01): "))

    total_inserted = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    if total_inserted >= cost:
        change = round(total_inserted - cost, 2)
        print(f"Payment successful! Your change: ${change}")
        return True
    else:
        print("Sorry, that's not enough money. Refunding coins.")
        return False


def make_coffee(drink):
    """Deducts resources to make the coffee."""
    for item in menu[drink]["ingredients"]:
        resources[item] -= menu[drink]["ingredients"][item]
    print(f"Here is your {drink}. Enjoy! ")


def coffee_machine():
    """Main function to run the Coffee Machine."""
    while True:
        print("\nCoffee Machine")
        print("Menu: espresso ($1.5), latte ($2.5), cappuccino ($3.0)")
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
        elif choice in menu:
            if check_resources(choice):
                if process_payment(menu[choice]["cost"]):
                    make_coffee(choice)
        else:
            print("Invalid choice. Please select espresso, latte, or cappuccino.")

coffee_machine()
