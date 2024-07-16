two_digit_number = str(input("enter a two digit number: "))

tens_digit = int(two_digit_number[0])
units_digit = int(two_digit_number[1])

sum_of_digits = tens_digit + units_digit

print(f"The sum of the digits in {two_digit_number} is {sum_of_digits}")