from random import randint
from FINAL_integer_checker_v4 import int_check

days = ["Rāhina", "Rātu", "Rāapa", "Rāpare", "Rāmere", "Rāhoroi", "Rātapu"]


def days_quiz_easy():
    random_number = randint(1, 7)
    print(random_number)
    question = f"Which day is {days[random_number - 1]}? (1-7) \n"
    answer = int_check(question, 1, 7)
    if answer == random_number:
        print("Your answer was correct, you got 1 point!")
        return True
    else:
        print("Your answer was incorrect, you have lost 1 life.")
        return False


def days_quiz_medium():
    random_number = randint(1, 7)
    print(random_number)
    question = f"Which day is {days[random_number - 1]}? (1-7) \n"
    answer = int_check(question, 1, 7)
    if answer == random_number:
        print("Your answer was correct, you got 1 point!")
        return True
    else:
        print("Your answer was incorrect, you have lost 1 life.")
        return False
