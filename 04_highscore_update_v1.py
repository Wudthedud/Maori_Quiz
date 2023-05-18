import shelve

d = shelve.open('score.txt')
numbers_highscore = d['highscores_numbers']
days_highscore = d['highscores_days']
months_highscore = d['highscores_months']
d.close()

number_scores = list(numbers_highscore)
days_scores = list(days_highscore)
months_scores = list(months_highscore)


def highscore_update(gamemode, name, score):
    if gamemode == 1 and score > number_scores:
        for i in range(5):
            if score > number_scores[i - 1]:
                number_scores.insert(i - 1, [name, score])
                del number_scores[-1]
    elif gamemode == 2 and score > days_highscore:
        for i in range(5):
            if score > days_scores[i - 1]:
                days_scores.insert(i - 1, [name, score])
                del days_scores[-1]
    elif gamemode == 3 and score > months_highscore:
        for i in range(5):
            if score > months_scores[i - 1]:
                months_scores.insert(i - 1, [name, score])
                del months_scores[-1]
    else:
        print("Good try but you did not manage to get a high score")
