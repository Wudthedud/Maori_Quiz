import shelve
d = shelve.open('score.txt')
numbers_highscore = d['highscores_numbers']
d.close()

# noinspection PyTypeChecker
scores = list(numbers_highscore)

scores.insert(2, ["Test1", 30])
del scores[-1]
print(scores)