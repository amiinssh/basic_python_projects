from art import logo

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def multiple(a, b):
    return a * b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operator():
    operators = {"ADD": add, "MINUS": minus, "DIVIDE": divide, "MULTIPLE": multiple}
    while True:
        op = input("ADD / MINUS / MULTIPLE / DIVIDE\n").upper()
        if op in operators:
            return op, operators[op]
        print("Invalid operator. Please enter a valid operator.")

def main():
    print(logo)
    while True:
        first_num = get_number("Please enter your first number: ")
        operator, operation = get_operator()
        second_num = get_number("Please enter your second number: ")

        result = operation(first_num, second_num)
        print(f"The result is: {result}")

        continue_choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
