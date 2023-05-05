import shelve

d = shelve.open('score.txt')
score = d['highscores_numbers']  # the score is read from disk
d.close()

print("High Scores")
for i in range(5):
    score_ = score[i]
    print(f"Name: {score_[0]}        Score: {score_[1]}")
