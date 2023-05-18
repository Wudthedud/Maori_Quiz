import shelve

d = shelve.open('score.txt')


d['highscores_numbers'] = ["Numbers_Player", 10]
d['highscores_days'] = ["Days_Player", 10]
d['highscores_months'] =  ["Months_player", 10]

d.close()