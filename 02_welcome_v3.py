from FINAL_yes_no_checker_v4 import yes_no
from FINAL_instructions_v2 import instructions

def welcome():
    name = input("Welcome to the Maori Language Quiz, what is your name? \n").lower().title()
    age = int(input(f"Hello {name}, how old are you? \n"))

    if age > 12:
        question = "You are too old for this game, would you like to continue?"
        if not yes_no(question):
            print("Farewell message")
            exit()
    elif age < 5:
        question = "You are too young for this game, would you like to continue?"
        if not yes_no(question):
            print("Farewell message")
            exit()
    question = "Have you played this game before?"

    if not yes_no(question):
        instructions()
