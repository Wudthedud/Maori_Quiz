"""Daniel Wu - Maori Quiz
Main Program - Version 2
Months quiz, looping, and score/lives system
"""
from FINAL_welcome_v4 import welcome
from FINAL_numbers_quiz_v3 import *
from FINAL_months_quiz_v4 import *
import shelve
from FINAL_highscore_update_v1 import *

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


d = shelve.open('score.txt')
numbers_highscore = d['highscores_numbers']
months_highscore = d['highscore_months']
days_highscore = d['highscore_days']
d.close()

if gamemode[0] == 1 and score > numbers_highscore[4[2]]:


