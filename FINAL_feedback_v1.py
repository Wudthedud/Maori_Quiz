from FINAL_yes_no_checker_v4 import yes_no
from FINAL_integer_checker_v4 import int_check
from FINAL_highscore_pull_v2 import *


def feedback():
    question = "Would you like to see the highscores?"
    if yes_no(question):
        scoreboard()
    question = "Would you like to play again?"
    if yes_no(question):
        return True
    else:
        return False
