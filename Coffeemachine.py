print("Welcome to the Coffeemachine")

remaining_milk = 300
remaining_water = 200
remaining_coffee = 100
money = 0

flavors = {
    "Espresso": [50, 18, 2.5],  # Water (ml), Caffeine (mg), Price ($)
    "Latte": [200, 24, 150, 3.5],  # Water (ml), Caffeine (mg), Milk (ml), Price ($)
    "Cappuccino": [
        250,
        24,
        100,
        1.75,
    ],  # Water (ml), Caffeine (mg), Milk (ml), Price ($)
}


user_order = input("Would you like Espresso, Latte, or Cappuccino? ")


def placing_order():
    while True:
        user_order = (
            input(
                "Would you like Espresso/Latte/Cappuccino, or would you like to see a report or turn off the machine? "
            )
            .strip()
            .capitalize()
        )

        if user_order == "Off":
            print("Turning off the machine. Goodbye!")
            break  # Exit the loop and terminate the program

        elif user_order == "Cappuccino":
            if (
                flavors["Cappuccino"][0] <= remaining_water
                and flavors["Cappuccino"][1] <= remaining_coffee
                and flavors["Cappuccino"][2] <= remaining_milk
            ):
                remaining_water -= flavors["Cappuccino"][0]
                remaining_coffee -= flavors["Cappuccino"][1]
                remaining_milk -= flavors["Cappuccino"][2]
                money += flavors["Cappuccino"][3]
                print("Here is a Cappuccino, enjoy!")
            else:
                print("Not enough ingredients for Cappuccino.")

        elif user_order == "Latte":
            if (
                flavors["Latte"][0] <= remaining_water
                and flavors["Latte"][1] <= remaining_coffee
                and flavors["Latte"][2] <= remaining_milk
            ):
                remaining_water -= flavors["Latte"][0]
                remaining_coffee -= flavors["Latte"][1]
                remaining_milk -= flavors["Latte"][2]
                money += flavors["Latte"][3]
                print("Here is a Latte, enjoy!")
            else:
                print("Not enough ingredients for Latte.")

        elif user_order == "Espresso":
            if (
                flavors["Espresso"][0] <= remaining_water
                and flavors["Espresso"][1] <= remaining_coffee
            ):
                remaining_water -= flavors["Espresso"][0]
                remaining_coffee -= flavors["Espresso"][1]
                money += flavors["Espresso"][2]
                print("Here is an Espresso, enjoy!")
            else:
                print("Not enough ingredients for Espresso.")

        elif user_order == "Report":
            print(
                f"Remaining coffee is {remaining_coffee}g, remaining milk is {remaining_milk}ml, and remaining water is {remaining_water}ml. The collected cash is {money}$."
            )

        else:
            print("Invalid input. Please try again.")


def process_coins():
    # Coin values in dollars
    penny_value = 0.01
    nickel_value = 0.05
    dime_value = 0.10
    quarter_value = 0.25

    # Ask for user input
    inputted_penny = int(input("How many Pennies?"))
    inputted_nickel = int(input("How many Nickels?"))
    inputted_dime = int(input("How many Dimes?"))
    inputted_quarter = int(input("How many Quarters?"))

    # Calculate total money inputted
    total_input = (
        (inputted_penny * penny_value)
        + (inputted_nickel * nickel_value)
        + (inputted_dime * dime_value)
        + (inputted_quarter * quarter_value)
    )

    # Price list based on the order
    prices = {
        "Espresso": flavors["Espresso"][2],
        "Cappuccino": flavors["Cappuccino"][3],
        "Latte": flavors["Latte"][3],
    }

    # Get the price for the selected order
    price = prices.get(user_order, 0)

    while total_input < price:
        print(f"Not enough money. You still need ${price - total_input:.2f}.")
        inputted_penny += int(input("How many more Pennies?"))
        inputted_nickel += int(input("How many more Nickels?"))
        inputted_dime += int(input("How many more Dimes?"))
        inputted_quarter += int(input("How many more Quarters?"))

        # Recalculate total money inputted
        total_input = (
            (inputted_penny * penny_value)
            + (inputted_nickel * nickel_value)
            + (inputted_dime * dime_value)
            + (inputted_quarter * quarter_value)
        )

    # If enough money is inputted
    placing_order()
    extra = total_input - price
    if extra > 0:
        print(f"Here is your change: ${extra:.2f}")
