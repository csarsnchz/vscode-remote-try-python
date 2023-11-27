#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
print("hello world")

# write rock, paper, scissors game received input from the user to the console
# and randomly choose rock, paper, or scissors for the computer
# and determine the winner and write the result to the console
# and wins the best of three games and write the result to the console
# and write the user choice and computer choice to the console
# and write the result to the console
# and write the winner to the console
# and write the loser to the console
# and write tie to the console
# and write invalid input to the console
# and write game over to the console
# and write goodbye to the console

import random
options = ["rock", "paper", "scissors"]
rounds_to_win = 3
user_score = 0
computer_score = 0
while user_score < rounds_to_win and computer_score < rounds_to_win:
    user_choice = input("Enter Rock, Paper, or Scissors: ")
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        print("User choice: " + user_choice)
        print("Computer choice: " + computer_choice)
        print("Tie!")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("User choice: " + user_choice)
            print("Computer choice: " + computer_choice)
            print("You lose!", computer_choice, "covers", user_choice)
            computer_score += 1
        else:
            print("User choice: " + user_choice)
            print("Computer choice: " + computer_choice)
            print("You win!", user_choice, "smashes", computer_choice)
            user_score += 1
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("User choice: " + user_choice)
            print("Computer choice: " + computer_choice)
            print("You lose!", computer_choice, "cut", user_choice)
            computer_score += 1
        else:
            print("User choice: " + user_choice)
            print("Computer choice: " + computer_choice)
            print("You win!", user_choice, "covers", computer_choice)
            user_score += 1
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("User choice: " + user_choice)
            print("Computer choice: " + computer_choice)
            print("You lose...", computer_choice, "smashes", user_choice)
            computer_score += 1
        else:
            print("User choice: " + user_choice)
            print("Computer choice: " + computer_choice)
            print("You win!", user_choice, "cut", computer_choice)
            user_score += 1
    else:
        print("User choice: " + user_choice)
        print("Invalid input!")
print("The final score is: User score: " + str(user_score) + " Computer score: " + str(computer_score))
if user_score > computer_score:
    print("You win!")
elif user_score == computer_score:
    print("Tie!")
else:
    print("You lose!")
print("Game over!")
print("Goodbye!")