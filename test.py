import shelve
from

d = shelve.open('score.txt')  # here you will save the score variable
d['score'] = 10            # thats all, now it is saved on disk.
d.close()

d = shelve.open('score.txt')
score = d['score']  # the score is read from disk
d.close()

print(score)

