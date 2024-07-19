print("Welcome to Python Pizza delivery!")

size = input("What size of Pizza do you want? S / M / L  ")

add_pepperoni = input("Do you want some pepperoni added? Yes / No  ")

extra_cheese = input("Do you want extra Cheese? Yes / No ")

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:  
    bill += 25


if add_pepperoni == "Yes":
    if size == "S":
        bill += 2
    else:  
        bill += 3


if extra_cheese == "Yes":
    bill += 1


print(f"Your total bill is {bill} $")