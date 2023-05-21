from FINAL_yes_no_checker_v4 import yes_no
from FINAL_highscore_pull_v2 import *


# Asks user if they want to see highscores and play again
def feedback():
    question = "Would you like to see the highscores?"
    if yes_no(question):
        scoreboard()
    question = "Would you like to play again?"
    if yes_no(question):
        return False
    else:
        return True
