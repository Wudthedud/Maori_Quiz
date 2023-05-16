"""Daniel Wu - Maori Quiz
Main Program - Version 3
Mo  nths quiz, looping, and score/lives system
"""
from FINAL_welcome_v4 import welcome
from FINAL_numbers_quiz_v3 import *
from FINAL_months_quiz_v4 import *
from FINAL_highscore_update_v2 import *
from FINAL_days_quiz_v3 import *

gamemode = welcome()
lives = 3
score = 0
result = None

while lives > 0:
    if gamemode[0] == 1:
        if gamemode[1] == 1:
            result = numbers_quiz_easy()
            print("You have chosen: Numbers Quiz - Easy")
        elif gamemode[1] == 2:
            result = numbers_quiz_medium()
            print("You have chosen: Numbers Quiz - Medium")
        else:
            result = numbers_quiz_hard()
            print("You have chosen: Numbers Quiz - Hard")
    elif gamemode[0] == 2:
        if gamemode[1] == 1:
            result = days_quiz_easy()
            print("You have chosen: Days Quiz - Easy")
        elif gamemode[1] == 2:
            result = days_quiz_medium()
            print("You have chosen: Days Quiz - Medium")
        else:
            result = days_quiz_hard()
            print("You have chosen: Days Quiz - Hard")
    else:
        if gamemode[1] == 1:
            result = months_quiz_easy()
            print("You have chosen: Months Quiz - Easy")
        elif gamemode[1] == 2:
            result = months_quiz_medium()
            print("You have chosen: Months Quiz - Medium")
        else:
            result = months_quiz_hard()
            print("You have chosen: Months Quiz - Hard")

    if result is True:
        score += 1
    elif result is False:
        lives -= 1

    print(f"Your score is: {score} points \n"
          f"You have {lives} lives left \n")

highscore_update(gamemode[0], gamemode[2], score)
print(f"You finsished with {score} points")

