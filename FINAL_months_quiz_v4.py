from random import randint
from FINAL_integer_checker_v4 import int_check
from FINAL_string_check_v4 import string_checker
from dictionary import dictionary_months

# List of months
months = ["Hanuere", "Pēpuere", "Maehe", "Āperira", "Mei", "Hune", "Hūrae",
          "Ākuhata", "Hepetema", "Ōketopa", "Noema", "Tīhema"]


# Easy quiz
def months_quiz_easy():
    random_number = randint(1, 6)
    question = f"Which month is {months[random_number - 1]}? (1-6) \n"
    answer = int_check(question, 1, 6)

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


# Medium Quiz
def months_quiz_medium():
    random_number = randint(1, 12)
    question = f"Which month is {months[random_number - 1]}? (1-12) \n"
    answer = int_check(question, 1, 12)

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


# Hard Quiz
def months_quiz_hard():
    random_number = randint(1, 12)
    print(f"What is the name of {dictionary_months[random_number]} in Maori?")
    choices = [months[random_number - 1]]
    while len(choices) < 4:
        choice = months[randint(0, 11)]
        if choice not in choices:
            choices.append(choice)
    from random import shuffle
    shuffle(choices)
    letters = ["A", "B", "C", "D"]

    for i in range(4):
        print(f"{letters[i]}: {choices[i]}")

    # Get the user's answer and check if it's correct
    while True:
        answer = string_checker("Enter the letter of your answer: (A/B/C/D)", 1, 1).upper().strip()
        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid input. Please enter A, B, C, or D.")

# Prints the user feedback with formatting
    if choices[letters.index(answer)] == months[random_number - 1]:
        print("=" * 64)
        print("\n" * 8)
        print("\033[92m" + "Your answer was correct, you got 1 point!\n" + "\033[0m")
        return True
    else:
        print("=" * 64)
        print("\n" * 8)
        print("\033[91m" + "Your answer was incorrect, you have lost 1 life.\n" + "\033[0m")
        return False
