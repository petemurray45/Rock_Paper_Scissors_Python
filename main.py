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

# Write your code below this line 👇

import random

user_choice = input("What do you choose? Type 'R' for Rock, 'P' for Paper, or 'S' for Scissors. ").lower()

if user_choice == 'r':
    print(rock)
elif user_choice == 'p':
    print(paper)
elif user_choice == "s":
    print(scissors)

print("Computer choses:")

computer_choice_random = random.randint(1, 3)

computer_choice_array = ["R", "P", "S"]
computer_choice_string = computer_choice_array[computer_choice_random]
computer_choice = computer_choice_string.lower()

if computer_choice == "r":
    print(rock)
elif computer_choice == "p":
    print(paper)
elif computer_choice == "s":
    print(scissors)

if user_choice == computer_choice:
    print("Draw! Try again.")
elif user_choice == "r":
    if computer_choice == "p":
        print("You lose! Paper beats rock.")
    else:
        print("You win! Rock beats scissors.")
elif user_choice == "p":
    if computer_choice == "s":
        print("You lose! Scissors beats paper.")
    else:
        print("You win! Paper beats rock.")
elif user_choice == "s":
    if computer_choice == "r":
        print("You lose! Rock beats scissors")
    else:
        print("You win! Scissors beats paper.")


