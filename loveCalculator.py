print("Welcome to love calculator!!")

name1 = input("what is your name?\n")

name2 = input("what is their name?\n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

num_of_T_name1 = lower_name1.count('t')
num_of_R_name1 = lower_name1.count('r')
num_of_U_name1 = lower_name1.count('u')
num_of_E_name1 = lower_name1.count('e')

num_of_L_name1 = lower_name1.count('l')
num_of_O_name1 = lower_name1.count('o')
num_of_V_name1 = lower_name1.count('v')
num_of_E_name1 += lower_name1.count('e') 

num_of_T_name2 = lower_name2.count('t')
num_of_R_name2 = lower_name2.count('r')
num_of_U_name2 = lower_name2.count('u')
num_of_E_name2 = lower_name2.count('e')

num_of_L_name2 = lower_name2.count('l')
num_of_O_name2 = lower_name2.count('o')
num_of_V_name2 = lower_name2.count('v')
num_of_E_name2 += lower_name2.count('e')  

total_T = num_of_T_name1 + num_of_T_name2
total_R = num_of_R_name1 + num_of_R_name2
total_U = num_of_U_name1 + num_of_U_name2
total_E = num_of_E_name1 + num_of_E_name2

total_L = num_of_L_name1 + num_of_L_name2
total_O = num_of_O_name1 + num_of_O_name2
total_V = num_of_V_name1 + num_of_V_name2
total_E += num_of_E_name2

first_digit = total_T + total_R + total_U + total_E
second_digit = total_L + total_O + total_V + total_E

compatibility_score = int(f"{first_digit}{second_digit}")

if compatibility_score <= 50:
    print("Better find sb else")
    print(f"Your compatibility score is {compatibility_score}")
else:
    print(f"Your compatibility score is {compatibility_score}")
    print("Your good to go")
