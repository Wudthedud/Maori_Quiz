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

selections = welcome()
gamemode = selections[0]
difficulty = selections[1]
name = selections[2]
repeat = True

while repeat:
    lives = 3
    score = 0
    result = None

    while lives > 0:
        if gamemode == 1:
            if difficulty == 1:
                result = numbers_quiz_easy()
            elif difficulty == 2:
                result = numbers_quiz_medium()
            else:
                result = numbers_quiz_hard()
        elif gamemode == 2:
            if difficulty == 1:
                result = days_quiz_easy()
            elif difficulty == 2:
                result = days_quiz_medium()
            else:
                result = days_quiz_hard()
        else:
            if difficulty == 1:
                result = months_quiz_easy()
            elif difficulty == 2:
                result = months_quiz_medium()
            else:
                result = months_quiz_hard()

        if result is True:
            score += 1
        elif result is False:
            lives -= 1

        print(f"Your score is: {score} points \n"
              f"You have {lives} lives left \n")

    highscore_update(gamemode, name, score)
    print(f"You finsished with {score} points")

    if feedback():
        print("Thanks for playing the Maori Quiz, hope you had fun and learned something. See you later!")
        repeat = False
        exit()
    else:
        continue
