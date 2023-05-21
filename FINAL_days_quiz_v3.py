from random import randint
from FINAL_integer_checker_v4 import int_check
from random import shuffle
from FINAL_string_check_v4 import string_checker
from dictionary import dictionary_days

# List of days
days = ["Rāhina", "Rātu", "Rāapa", "Rāpare", "Rāmere", "Rāhoroi", "Rātapu"]


# Code for the easy quiz
def days_quiz_easy():
    random_number = randint(1, 4)
    question = f"Which day is {days[random_number - 1]}? (1-4) \n"
    answer = int_check(question, 1, 4)
    if answer == random_number:
        print("=" * 64)
        print("\n" * 8)
        print("\033[92m" + "Your answer was correct, you got 1 point!\n" + "\033[0m")
        return True
    else:
        print("=" * 64)
        print("\n" * 8)
        print("\033[91m" + "Your answer was incorrect, you have lost 1 life.\n" + "\033[0m")
        return False


# Code for the medium quiz
def days_quiz_medium():
    random_number = randint(1, 7)
    question = f"Which day is {days[random_number - 1]}? (1-7) \n"
    answer = int_check(question, 1, 7)
    if answer == random_number:
        print("=" * 64)
        print("\n" * 8)
        print("\033[92m" + "Your answer was correct, you got 1 point!\n" + "\033[0m")
        return True
    else:
        print("=" * 64)
        print("\n" * 8)
        print("\033[91m" + "Your answer was incorrect, you have lost 1 life.\n" + "\033[0m")
        return False


# Code for the hard quiz
def days_quiz_hard():
    random_number = randint(1, 7)
    print(f"What is the name of {dictionary_days[random_number]} in Maori?")
    choices = [days[random_number - 1]]
    while len(choices) < 4:
        choice = days[randint(0, 6)]
        if choice not in choices:
            choices.append(choice)
    shuffle(choices)
    letters = ["A", "B", "C", "D"]
    for i in range(4):
        print(f"{letters[i]}: {choices[i]}")

    # Get the user's answer and check if it's correct
    while True:
        answer = string_checker("Enter the letter of your answer: (A/B/C/D) ", 1, 1).upper().strip()
        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid input. Please enter A, B, C, or D.")

# Gives user feedback
    if choices[letters.index(answer)] == days[random_number - 1]:
        print("=" * 64)
        print("\n" * 8)
        print("\033[92m" + "Your answer was correct, you got 1 point!\n" + "\033[0m")
        return True
    else:
        print("=" * 64)
        print("\n" * 8)
        print("\033[91m" + "Your answer was incorrect, you have lost 1 life.\n" + "\033[0m")
        return False
