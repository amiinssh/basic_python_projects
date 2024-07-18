"""Plays a game where the user must type words within a time limit."""

import typer
import time
import random

print("Type the words and hit enter within the time limit!")

max_level = 5
player_level = 1

for level in range(1, max_level + 1):
    print("Level " + str(level))
    params = typer.get_level_parameters(level)
    words_to_type = typer.pick_random_words(params["num_words"], params["difficulty"])
    passed = typer.play_round(words_to_type, params["time_limit"])
    if not passed:
        print("Oops! You didn't make it past level " + str(level) + ".")
        break
    player_level = level

print("Thanks for playing.")
print("You reached level " + str(player_level) + ".")
