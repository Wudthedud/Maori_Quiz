import shelve

d = shelve.open('score.txt')
numbers_highscore = d['highscores_numbers']
days_highscore = d['highscores_days']
months_highscore = d['highscores_months']
d.close()


def scoreboard_numbers():
    print("High Scores")
    for i in range(5):
        scores = numbers_highscore[i]
        print(f"Name: {scores[0]}        Score: {scores[1]}")


def scoreboard_days():
    print("High Scores")
    for i in range(5):
        scores = days_highscore[i]
        print(f"Name: {scores[0]}        Score: {scores[1]}")


def scoreboard_months():
    print("High Scores")
    for i in range(5):
        scores = months_highscore[i]
        print(f"Name: {scores[0]}        Score: {scores[1]}")
