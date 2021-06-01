MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "water": 400,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def report():
    """Prints a report of resources available and money collected"""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')


def check_levels(drink):
    """Checks the level of resources before making a drink. Returns an error message
    if there isn't enough of a given resource to fulfill the order."""
    for resource in resources:
        if resources[resource] >= MENU[drink]['ingredients'][resource]:
            return True
        else:
            print(f'Sorry, there is not enough {resource}.')
            return False


def check_change(drink, quarters, dimes, nickels, pennies):
    """Converts the coins to dollar amounts, calculates if there is enough to purchase the drink, and returns
    either the change or an error message if the funds are short."""
    quarters = quarters * .25
    dimes = dimes * .10
    nickels = nickels * .05
    pennies = pennies * .01

    entered_amount = quarters + dimes + nickels + pennies
    if entered_amount >= MENU[drink]['cost']:
        return round(entered_amount - MENU[drink]['cost'], 2)
    else:
        return -1


def update_resources(drink):
    """Updates the resources once an order is complete."""
    resources['money'] += MENU[drink]['cost']
    resources['milk'] -= MENU[drink]['ingredients']['milk']
    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']


def vend():
    """The main function of the program."""
    should_continue = True
    while should_continue:
        coffee_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if coffee_choice == 'off':
            print('Shutting down.')
            break
        if coffee_choice == 'report':
            report()
        else:
            check1 = check_levels(coffee_choice)
            if check1:
                print('Please insert coins.')
                quarters = int(input('How many quarters? '))
                dimes = int(input('How many dimes? '))
                nickels = int(input('How many nickels? '))
                pennies = int(input('How many pennies? '))

                check2 = check_change(coffee_choice, quarters, dimes, nickels, pennies)
                if check2 >= 0:
                    print(f'Here is ${check2} in change.')
                    print(f'Here is your {coffee_choice}. Enjoy!')
                    update_resources(coffee_choice)

                else:
                    print('Sorry, that\'s not enough money. Money refunded.')

            else:
                continue


vend()
