total_bill = int(input("What was the total bill? $ "))

percentage_of_tips = int(input("What percentage of tips would you give? "))

num_of_people = int(input("How many people are spitting the bill? "))

tip = total_bill * (percentage_of_tips / 100)

total_bill_with_tip = total_bill + tip

each_must_pay = total_bill_with_tip / num_of_people

each_must_pay = round(each_must_pay, 2)

print(f"Each person must pay $ {each_must_pay}")