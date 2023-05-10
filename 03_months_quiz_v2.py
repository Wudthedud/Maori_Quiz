from random import randint
from FINAL_integer_checker_v4 import int_check

months = ["Kohi-tātea", "Hui-tanguru", "Poutū-te-rangi", "Paenga-whāwhā", "Haratua", "Pipiri", "Hōngongoi",
          "Here-turi-kōkā", "Mahuru", "Whiringa-ā-nuku", "Whiringa-ā-rangi", "Hakihea"]


def months_quiz_easy():
    random_number = randint(1, 5)
    print(random_number)
    question = f"Which month is {months[random_number - 1]}? (1-6) \n"
    answer = int_check(question, 1, 6)

    if answer == random_number:
        print("Your answer was correct, you got 1 point!")
        return True
    else:
        print("Your answer was incorrect, you have lost 1 life.")
        return False


def months_quiz_medium():
    random_number = randint(1, 12)
    print(random_number)
    question = f"Which month is {months[random_number - 1]}? (1-12) \n"
    answer = int_check(question, 1, 12)

    if answer == random_number:
        print("Your answer was correct, you got 1 point!")
        return True
    else:
        print("Your answer was incorrect, you have lost 1 life.")
        return False
