import shelve

d = shelve.open('score.txt')  # here you will save the score variable
d['highscores_numbers'] = [["User1", 10], ["User2", 9], ["User3", 8], ["User4", 7], ["User5", 6]]
d['highscores_months'] = [["User1", 10], ["User2", 9], ["User3", 8], ["User4", 7], ["User5", 6]]
d['highscores_days'] = [["User1", 10], ["User2", 9], ["User3", 8], ["User4", 7], ["User5", 6]]
d.close()

