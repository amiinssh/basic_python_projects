rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

user_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors")

for _ in range(3):
    user_choice = input("Rock / Paper / Scissors: ").lower()

    if user_choice == "rock":
        print(f"user choice {rock}")
    elif user_choice == "paper":
        print(f"user choice {paper}")
    elif user_choice == "scissors":
        print(f"user choice {scissors}")
    else:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        continue

    computer_choice = ["rock", "paper", "scissors"]
    choice = random.choice(computer_choice)

    if choice == "rock":
        print(f"computer choice {rock}")
    elif choice == "paper":
        print(f"computer choice {paper}")
    else:
        print(f"computer choice {scissors}")

    if user_choice == choice:
        print("Draw")
    elif (user_choice == "rock" and choice == "scissors") or \
         (user_choice == "paper" and choice == "rock") or \
         (user_choice == "scissors" and choice == "paper"):
        print("User won!")
        user_score += 1
    else:
        print("Computer won!")
        computer_score += 1

print("----------")
print(f'Final scores:')
print(f'Your score: {user_score}')
print(f'Computer score: {computer_score}')

if user_score == computer_score:
    print('DRAW')
elif user_score > computer_score:
    print('YOU WON')
else:
    print('COMPUTER WON')