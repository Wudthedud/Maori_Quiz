from FINAL_yes_no_checker_v4 import yes_no

name = input("Welcome to the Maori Language Quiz, what is your name? \n")
age = int(input(f"Hello {name.title()}, how old are you? \n "))

if age > 12:
    question = "You are too old for this game, would you like to continue?"
    yes_no(question)
elif age < 5:
    question = "You are too young for this game, would you like to continue? (Y/N)"
    yes_no(question)
