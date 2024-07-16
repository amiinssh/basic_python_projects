weight = input("Please enter your weight in KG: ")
height = input("Please enter your height in meters: ")

weight = float(weight)
height = float(height)

BMI = weight / height ** 2

if BMI <= 18.5:
    print("you are underweight")
elif BMI <= 24.9:    
    print("you are healthy")
elif BMI <= 29.9:    
    print("you are overweight")
elif BMI > 30:    
    print("you are obese")


print(f"Your BMI is {BMI:.2f}")




    #If your BMI is less than 18.5, it falls within the underweight range.
    #If your BMI is 18.5 to 24.9, it falls within the Healthy Weight range.
    #If your BMI is 25.0 to 29.9, it falls within the overweight range.
    #If your BMI is 30.0 or higher, it falls within the obese range.
