from random import randint
from FINAL_string_check_v4 import string_checker
from dictionary import dictionary_months

months = ["Hanuere", "Pēpuere", "Maehe", "Āperira", "Mei", "Hune", "Hūrae",
          "Ākuhata", "Hepetema", "Ōketopa", "Noema", "Tīhema"]

def months_quiz_multiple_choice():
    random_number = randint(1, 12)
    print(f"What is the name of {dictionary_months[random_number]} in Maori?")

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
    question = "Enter the letter of your answer: ", ["A", "B", "C", "D"]
    answer = string_checker(question, 1, 1).upper()
    if choices[letters.index(answer)] == months[random_number - 1]:
        print("Your answer was correct, you got 1 point!")
        return True
    else:
        print("Your answer was incorrect, you have lost 1 life.")
        return False


months_quiz_multiple_choice()
