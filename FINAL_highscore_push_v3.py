import shelve


def update_scores(numbers, days, months):
    d = shelve.open('score.txt')  # here you will save the score variable
    d['highscores_numbers'] = numbers
    d['highscores_months'] = days
    d['highscores_days'] = months
    d.close()
