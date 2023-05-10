from FINAL_welcome_v4 import welcome
from FINAL_numbers_quiz_v3 import *

gamemode = welcome()
lives = 3
score = 0
result = None
while lives > 0:
    print(gamemode)
    if gamemode[0] == 1:
        if gamemode[1] == 1:
            result = numbers_quiz_easy()

        elif gamemode[1] == 2:
            result = numbers_quiz_medium()
        else:
            result = numbers_quiz_hard()
    elif gamemode[0] == 2:
        result =

    if result is True:
        score += 1
    else:
        lives -= 1

    print(f"Your score is: {score} points \n"
          f"You have {lives} lives left \n")

