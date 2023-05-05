import shelve

d = shelve.open('score.txt')
score = d['highscores_numbers']  # the score is read from disk
d.close()

print("\t High Scores:")
for i in range(5):
    score_ = score[i]
    print(f"{score_[0]}          {score_[1]} points")

