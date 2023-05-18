from FINAL_yes_no_checker_v4 import yes_no
from FINAL_instructions_v2 import instructions
from FINAL_integer_checker_v4 import int_check
from FINAL_string_check_v4 import string_checker

GAME_MODES = ["Numbers Quiz", "Days of the Week Quiz", "Months Quiz"]
DIFFICULTIES = ["Easy", "Medium", "Hard"]


def welcome():
    name = string_checker("Welcome to the Maori Language Quiz, what is your name?", 1, 10).lower().title()
    question = f"Hello {name}, how old are you? \n"
    age = int_check(question, 1, 100)

    if age > 12:
        question = "You are too old for this game, would you like to continue?"
        if not yes_no(question):
            print("Farewell message")
            exit()
    elif age < 5:
        question = "You are too young for this game, would you like to continue?"
        if not yes_no(question):
            print("Thanks for trying out this quiz, see you later!")
            exit()
    question = "Have you played this game before?"

    if not yes_no(question):
        instructions()
        question = "Do you wish to continue?"
        if not yes_no(question):
            print("Thanks for trying out this quiz, see you later!")
            exit()

    question = ("Choose a quiz: \n"
                "1. \t Maori Numbers Quiz \n"
                "2. \t Days of the week in Maori Quiz \n"
                "3. \t Months in Maori Quiz \n")
    game_mode = int_check(question, 1, 3)

    question = ("\nChoose a difficulty: \n"
                "1. \t Easy \n"
                "2. \t Medium \n"
                "3. \t Hard \n")
    difficulty = int_check(question, 1, 3)

    print("\n" * 60)
    print(f"You are playing {GAME_MODES[game_mode - 1]} - {DIFFICULTIES[difficulty - 1]}")
    game = [game_mode, difficulty, name]
    return game
