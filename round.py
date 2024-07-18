import random

"""Supports a round of rock, paper, scissors between a user and a computer."""

def make_user_choice():
    valid_choices = ["rock", "paper", "scissors"]
    user_input = input("Choose one: rock, paper, or scissors? ").lower()
    
    while user_input not in valid_choices:
        print("Invalid choice. Please try again.")
        user_input = input("Choose one: rock, paper, or scissors? ").lower()
    
    return user_input
    

def make_computer_choice():
    game = random.randint(1, 3)
    if game == 1:
        return "scissors"
    elif game == 2:
        return "rock"
    else:
        return "paper"
    """Returns the computer's choice of rock, paper, or scissors.
    The computer chooses randomly, with each choice equally likely.
    """
    

def wins_matchup(choice, opponent_choice):
    if choice == "rock" and opponent_choice == "scissors":
        return True
    elif choice == "scissors" and opponent_choice == "paper":
        return True
    elif choice == "paper" and opponent_choice == "rock":
        return True
    else:
        return False

def format_score(user_score, computer_score):
    """Returns a formatted version of the players's current scores."""
    user = "user (" + str(user_score) + ")"
    computer = "computer (" + str(computer_score) + ")"
    return user + " vs. " + computer