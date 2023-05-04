import shelve

d = shelve.open('score.txt')  # here you will save the score variable
d['score_numbers'] = 30            # thats all, now it is saved on disk.
d.close()

d = shelve.open('score.txt')
score = d['score_numbers']  # the score is read from disk
d.close()

print(score)

