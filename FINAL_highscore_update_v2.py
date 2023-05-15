import shelve
from FINAL_highscore_pull_v1 import *
from FINAL_highscore_push_v3 import *

d = shelve.open('score.txt')
numbers_highscore = d['highscores_numbers']
days_highscore = d['highscores_days']
months_highscore = d['highscores_months']
d.close()

number_scores = list(numbers_highscore)  # noqa
days_scores = list(days_highscore)  # noqa
months_scores = list(months_highscore)  # noqa


def highscore_update(gamemode, name, score):
    print("You got a high score!")
    if gamemode == 1 and score > list(number_scores[4])[1]:
        for i in range(5):
            if score > (number_scores[i - 1])[1]:
                number_scores.insert(i - 1, [name, score])
                del number_scores[-1]
                break

    elif gamemode == 2 and score > list(days_scores[4])[1]:
        print("You got a high score!")
        for i in range(5):
            if score > (days_scores[i - 1])[1]:
                days_scores.insert(i - 1, [name, score])
                del days_scores[-1]
                break

    elif gamemode == 3 and score > list(months_scores[4])[1]:
        print("You got a high score!")
        for i in range(5):
            if score > months_scores[i - 1][1]:
                months_scores.insert(i - 1, [name, score])
                del months_scores[-1]
                break

    d = shelve.open('score.txt')
    d['highscores_numbers'] = number_scores
    d['highscores_months'] = days_scores
    d['highscores_days'] = months_scores
    d.close()