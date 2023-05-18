import shelve

d = shelve.open('score.txt')

numbers_highscore = d['highscores_numbers']
days_highscore = d['highscores_days']
months_highscore = d['highscores_months']


def update_scores(gamemode, name, score):
    if gamemode == 1 and score > numbers_highscore[1]:
        d['highscores_numbers'] = [name, score]
    elif gamemode == 2 and score > days_highscore[1]:
        d['highscores_days'] = [name, score]
    elif gamemode == 3 and score > months_highscore[1]:
        d['highscores_months'] = [name, score]
    d.close()


update_scores(1, 'Daniel', 11)
