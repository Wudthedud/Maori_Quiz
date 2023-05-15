"""Daniel Wu - Highscore Pull (Gets highscores and displays them)
"""
import shelve
from string_formatter import *

# Pulls highscores from the score.txt file and makes them into varaibles using shelve
d = shelve.open('score.txt')
numbers_highscore = d['highscores_numbers']
days_highscore = d['highscores_days']
months_highscore = d['highscores_months']
d.close()


# Sorts the scoreboard by the scores and prints them out for the numbers scorebaord
def scoreboard_numbers():
    sorted_scores = sorted(numbers_highscore, key=lambda x: x[1], reverse=True)  # noqa
    print("Top 5 High Scores".center(50, "."))
    for i in range(5):
        scores = sorted_scores[i]
        print(f"{scores[0]} --- {scores[1]} points".center(50, " "))


# Sorts the scoreboard by the scores and prints them out for the days scorebaord
def scoreboard_days():
    sorted_scores = sorted(days_highscore, key=lambda x: x[1], reverse=True)  # noqa
    print("Top 5 High Scores".center(50, "."))
    for i in range(5):
        scores = sorted_scores[i]
        print(f"{scores[0]} --- {scores[1]} points".center(50, " "))


# Sorts the scoreboard by the scores and prints them out for the months scorebaord
def scoreboard_months():
    sorted_scores = sorted(months_highscore, key=lambda x: x[1], reverse=True)  # noqa
    print("Top 5 High Scores".center(50, "."))
    for i in range(5):
        scores = sorted_scores[i]
        print(f"{scores[0]} --- {scores[1]} points".center(50, " "))
