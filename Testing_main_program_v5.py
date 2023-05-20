"""Daniel Wu - Maori Quiz
Main Program - Version 5 (Completed Version)
Final Touches, aestetics and bug fixes
"""
from FINAL_welcome_v4 import *
from FINAL_numbers_quiz_v3 import *
from FINAL_months_quiz_v4 import *
from FINAL_highscore_update_v2 import *
from FINAL_days_quiz_v3 import *
from FINAL_feedback_v1 import *

# Variables


repeat = True

# Looping the code while the user still has more than 1 life
while repeat:
    lives = 3
    score = 0
    result = None

    # Prompting the user the questions
    for i in range(12):
        score += 1
        print("\033[4m" + "\033[94m" + f"{score} point(s)                     {lives} live(s)" + "\033[0m")

    for i in range(3):
        lives -= 1
        print("\033[4m" + "\033[94m" + f"{score} point(s)                     {lives} live(s)" + "\033[0m")

    # Updates the highscore using a function  and telling user how many points the got

    print(f"You finsished with {score} points")

    if feedback():
        print("Thanks for playing the Maori Quiz, hope you had fun and learned something. See you later!")
        repeat = False
        exit()
    else:
        continue
