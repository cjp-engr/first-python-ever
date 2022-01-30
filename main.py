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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def user_selects_option():
    while True:
        user_entered = input("What would you like? (espresso/latte/cappuccino): ")
        user_entered_lowered_case = user_entered.lower().strip()

        if user_entered_lowered_case == "espresso":
            user_entered_espresso()
        elif user_entered_lowered_case == "latte":
            user_entered_latte()
        elif user_entered_lowered_case == "cappuccino":
            user_entered_cappuccino()
        elif user_entered_lowered_case == "report":
            user_entered_report()
        elif user_entered_lowered_case == "off":
            print("I am turned off, bye!")
            break
        else:
            print("you entered a wrong keyword. please try again.")


def user_entered_espresso():
    print("espresso")
    check_available_resources("espresso")


def user_entered_latte():
    print("latte")
    check_available_resources("latte")


def user_entered_cappuccino():
    print("cappuccino")
    check_available_resources("cappuccino")


def user_entered_report():
    for key, value in resources.items():
        if key == "water":
            print("Water: ", value, "ml")
        elif key == "milk":
            print("Milk: ", value, "ml")
        elif key == "coffee":
            print("Coffee: ", value, "g")
    print("Money : $", profit)


def check_available_resources(user_entered):
    coffee_ingredients = MENU[user_entered]["ingredients"]
    is_user_inserted_coins = False

    for key, value in coffee_ingredients.items():

        if resources[key] < coffee_ingredients[key]:
            print("Sorry there is not enough ", key)
            break
            # is_item_enough = False
            # if not is_item_enough:
            #     print("Sorry there is not enough ", key)
            #     print(is_item_enough)
            #     break

        else:
            if not is_user_inserted_coins:
                quarter_count = float(input("Insert quarter: "))
                dimes_count = float(input("Insert dimes: "))
                nickels_count = float(input("Insert nickels: "))
                pennies_count = float(input("Insert pennies: "))
                inserted_coins(user_entered, quarter_count, dimes_count, nickels_count, pennies_count)
                is_user_inserted_coins = True

            resources[key] = resources[key] - coffee_ingredients[key]


def inserted_coins(user_entered, quarter_count, dimes_count, nickels_count, pennies_count):
    quarters = 0.25
    dimes = 0.10
    nickels = 0.05
    pennies = 0.01
    product_cost = MENU[user_entered]["cost"]
    global profit

    amount_entered = (quarters * quarter_count) + (dimes * dimes_count) + (nickels * nickels_count) + \
                     (pennies * pennies_count)

    if amount_entered <= product_cost:
        print("You entered insufficient amount")
    elif amount_entered == product_cost:
        print("You entered exact amount")
        profit += product_cost
    else:
        amount_change = amount_entered - product_cost
        profit += product_cost
        print("Your change: ", round(amount_change, 2))


user_selects_option()
