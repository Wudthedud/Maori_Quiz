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


def months_quiz_multiple_choice():
    random_number = randint(1, 12)
    print(f"Which month is {months[random_number - 1]}?")

    # Create a list of multiple choices, which includes the correct answer
    choices = [months[random_number - 1]]
    while len(choices) < 4:
        choice = months[randint(0, 11)]
        if choice not in choices:
            choices.append(choice)

    # Shuffle the choices and assign them to letters
    from random import shuffle
    shuffle(choices)
    letters = ["A", "B", "C", "D"]

    # Print the multiple choices
    for i in range(4):
        print(f"{letters[i]}: {choices[i]}")

    # Get the user's answer and check if it's correct
    answer = str_check("Enter the letter of your answer: ", ["A", "B", "C", "D"])
    if choices[letters.index(answer)] == months[random_number - 1]:
        print("Your answer was correct, you got 1 point!")
        return True
    else:
        print("Your answer was incorrect, you have lost 1 life.")
        return False
