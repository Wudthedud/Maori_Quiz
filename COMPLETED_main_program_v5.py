"""Daniel Wu - Maori Quiz
Main Program - Version 5 (Completed Version)
Final Touches, aestetics and bug fixes
"""
from FINAL_welcome_v4 import *
from FINAL_numbers_quiz_v3 import *
from FINAL_months_quiz_v4 import *
from highscore_update_v2 import *
from FINAL_days_quiz_v3 import *
from FINAL_feedback_v1 import *

# Variables
selections = welcome()
gamemode = selections[0]
difficulty = selections[1]
name = selections[2]
repeat = True

# Looping the code while the user still has more than 1 life
while repeat:
    lives = 3
    score = 0
    result = None

    # Prompting the user the questions
    while lives > 0:
        print("\033[4m" + "\033[94m" + f"{score} point(s)                     {lives} live(s)" + "\033[0m")

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

    # Updates the highscore using a function  and telling user how many points the got
    update_scores(gamemode, name, score)
    print(f"You finished with {score} points")

# Checks if they want to see scoreboard and if they want to play again, repeats or exits program accordingly
    if feedback():
        print("Thanks for playing the Maori Quiz, hope you had fun and learned something. See you later!")
        repeat = False
        exit()
    else:
        continue
