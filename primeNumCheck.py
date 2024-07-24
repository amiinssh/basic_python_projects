print("Welcome to the prime number indicator")

n = int(input("Check this number: "))

def prime_checker(number):
    if number <= 1:
        print("Number was not PRIME")
        return

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print("Number was not PRIME")
            return

    print("Number was PRIME")

prime_checker(number=n)

