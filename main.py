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
machine_on = True

def resources_available(x):
    if x == 'report':
        return resources['water'], resources['milk'], resources['coffee']
    elif resources['water'] < MENU[x]['ingredients']['water'] :
        print('Sorry there is not enough water')
        return False
    elif resources['coffee'] < MENU[x]['ingredients']['coffee']:
        print('Sorry there is not enough coffee')
        return False
    elif x != 'espresso':
        if resources['milk'] < MENU[x]['ingredients']['milk']:
            print('Sorry there is not enough milk')
            return False


def menu_display():
    print('*' * 35)
    print(f'   Welcome to XYZ coffee Shop  ')
    print('*' * 35)
    print(f"Menu" + " " * 23 + "Price($)")
    print('*' * 35)
    for drinks in MENU:
        char = 30 - len(drinks)
        print(f"{drinks}" + " " * char + f"${MENU[drinks]['cost']}")
    print('*' * 35)

def get_user_choice():
    options = ["espresso", "latte", "cappuccino", "off", "report"]
    user_choice = input("\nWhat would you like?/(espresso/latte/cappuccino): ").lower()

    if user_choice in options:
        return user_choice
    elif user_choice == 'report':

    else:
        print("Invalid entry. Please choose from  espresso, latte, or cappuccino.")
        return get_user_choice()

while machine_on:

    menu_display()

    choice = get_user_choice()

    if choice == "report":
       water,milk,coffee = resources_available(x='report')
       print(f'Water: {water}\n'
                 f'Milk: {milk}\n'
                    f'Coffee: {coffee}\n')

    check_resources = resources_available(choice)
    if check_resources == 'False':
        machine_on = False
        break
    # else:
        # process_coin()
