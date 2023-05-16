"""Daniel Wu - Maori Quiz
Main Program - Version 3
Mo  nths quiz, looping, and score/lives system
"""
from FINAL_welcome_v4 import welcome
from FINAL_numbers_quiz_v3 import *
from FINAL_months_quiz_v4 import *
from FINAL_highscore_update_v2 import *
from FINAL_yes_no_checker_v4 import yes_no

gamemode = welcome()
lives = 3
score = 0
result = None

while lives > 0:
    if gamemode[0] == 1:
        if gamemode[1] == 1:
            result = numbers_quiz_easy()
        elif gamemode[1] == 2:
            result = numbers_quiz_medium()
        else:
            result = numbers_quiz_hard()
    elif gamemode[0] == 3:
        if gamemode[1] == 1:
            result = months_quiz_easy()
        elif gamemode[1] == 2:
            result = months_quiz_medium()
        else:
            result = months_quiz_hard()
    else:
        if gamemode[1] == 1:
            result = months_quiz_easy()
        elif gamemode[1] == 2:
            result = months_quiz_medium()
        else:
            result = months_quiz_hard()

    if result is True:
        score += 1
    elif result is False:
        lives -= 1

    print(f"Your score is: {score} points \n"
          f"You have {lives} lives left \n")

highscore_update(gamemode[0], gamemode[2], score)
print(f"You finsished with {score} points")
