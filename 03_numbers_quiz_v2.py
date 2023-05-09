from random import randint
from FINAL_integer_checker_v4 import int_check

numbers = ["tahi", "rua", "toru", "whā", "rima", "ono", "whitu", "waru", "iwa", "tekau"]


def numbers_quiz_easy():
    random_number = randint(1, 5)
    print(random_number)
    question = f"Which number is {numbers[random_number - 1]}? (1-5) \n"
    answer = int_check(question, 1, 5)

    if answer == random_number:
        print("Your answer was correct, you got 1 point!")
        return True
    else:
        print("Your answer was incorrect, you have lost 1 life.")
        return False


def numbers_quiz_medium():
    random_number = randint(1, 10)
    print(random_number)
