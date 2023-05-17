from FINAL_yes_no_checker_v4 import yes_no
from FINAL_integer_checker_v4 import int_check
from FINAL_highscore_pull_v1 import *


def feedback():
    question = "Would you like to see the highscores?"
    if yes_no(question):
        question = "Which scoreboard would you like to see? \n" \
                   "1. Numbers Quiz Scoreboard \n" \
                   "2. Days of Week Quiz Scoreboard \n" \
                   "3. Months Quiz Scoreboard\n"
        scoreboard_selection = int_check(question, 1, 3)
        if scoreboard_selection == 1:
            scoreboard_numbers()
        elif scoreboard_selection == 2:
            scoreboard_days()
        else:
            scoreboard_months()

    question = "Would you like to play again?"
    if yes_no(question):
        return False
    else:
        return True