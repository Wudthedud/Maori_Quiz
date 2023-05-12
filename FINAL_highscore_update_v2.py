import shelve
from FINAL_highscore_pull_v1 import *

d = shelve.open('score.txt')
numbers_highscore = d['highscores_numbers']
days_highscore = d['highscores_days']
months_highscore = d['highscores_months']
d.close()

number_scores = list(numbers_highscore)  # noqa
days_scores = list(days_highscore)  # noqa
months_scores = list(months_highscore)  # noqa


def highscore_update(gamemode, name, score):
    if gamemode == 1 and score > list(numbers_highscore[4])[1]:
        for i in range(5):
            if score > list(numbers_highscore[i - 1])[1]:
                list(numbers_highscore).insert(i - 1, [name, score])
                del list(numbers_highscore[-1])
                print("You got a high score!")
                scoreboard_numbers()

    elif gamemode == 2 and score > list(days_scores[4])[1]:
        for i in range(5):
            if score > days_scores[i - 1]:
                days_scores.insert(i - 1, [name, score])
                del days_scores[-1]
                print("You got a high score!")
                scoreboard_days()

    elif gamemode == 3 and score > list(months_scores[4])[1]:
        for i in range(5):
            if score > months_scores[i - 1]:
                months_scores.insert(i - 1, [name, score])
                del months_scores[-1]
                print("You got a high score!")
                scoreboard_months()


print(numbers_highscore)
print(number_scores)
print(list(number_scores[4])[1])