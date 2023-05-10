from FINAL_welcome_v4 import welcome
from FINAL_numbers_quiz_v3 import *

gamemode = welcome()

print(gamemode)
if gamemode[0] == 1:
    if gamemode[1] == 1:
        result = numbers_quiz_easy()
    elif gamemode[1] == 2:
        result = numbers_quiz_medium()
    else:
        result = numbers_quiz_hard()
