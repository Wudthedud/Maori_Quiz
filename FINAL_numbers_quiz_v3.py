from random import randint
from FINAL_integer_checker_v4 import int_check

numbers = ["tahi", "rua", "toru", "whā", "rima", "ono", "whitu", "waru", "iwa", "tekau", "tekau mā Tahi",
           "tekau mā rua", "tekau mā toru", "tekau mā whā", "tekau mā rima", "tekau mā ono", "tekau mā whitu",
           "tekau mā waru", "tekau mā iwa", "rua tekau"]


def numbers_quiz_easy():
    random_number = randint(1, 5)
    question = f"Which number is {numbers[random_number - 1]}? (1-5) \n"
    answer = int_check(question, 1, 5)

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


def numbers_quiz_medium():
    random_number = randint(1, 10)
    question = f"Which number is {numbers[random_number - 1]}? (1-10) \n"
    answer = int_check(question, 1, 10)

    if answer == random_number:
        print("=" * 32)
        print("\n" * 9)
        print("\033[92m" + "Your answer was correct, you got 1 point!\n" + "\033[0m")
        return True
    else:
        print("\n" * 9)
        print("\033[91m" + "Your answer was incorrect, you have lost 1 life.\n" + "\033[0m")
        print("=" * 32)
        return False


def numbers_quiz_hard():
    random_number = randint(1, 20)
    question = f"Which number is {numbers[random_number - 1]}? (1-20) \n"
    answer = int_check(question, 1, 20)

    if answer == random_number:
        print("\033[92m" + "Your answer was correct, you got 1 point!" + "\033[0m")
        return True
    else:
        print("\033[91m" + "Your answer was incorrect, you have lost 1 life." + "\033[0m")
        return False
