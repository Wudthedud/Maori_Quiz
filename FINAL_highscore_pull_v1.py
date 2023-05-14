import shelve

d = shelve.open('score.txt')
numbers_highscore = d['highscores_numbers']
days_highscore = d['highscores_days']
months_highscore = d['highscores_months']
d.close()


def scoreboard_numbers():
    sorted_scores = sorted(numbers_highscore, key=lambda x: x[1], reverse=True)  # noqa
    print("Top 5 High Scores")
    for i in range(5):
        scores = sorted_scores[i]
        print(f"Name: {scores[0]}        Score: {scores[1]}")


def scoreboard_days():
    sorted_scores = sorted(days_highscore, key=lambda x: x[1], reverse=True)  # noqa
    print("High Scores")
    for i in range(5):
        scores = sorted_scores[i]
        print(f"Name: {scores[0]}        Score: {scores[1]}")


def scoreboard_months():
    sorted_scores = sorted(months_highscore, key=lambda x: x[1], reverse=True)  # noqa
    print("High Scores")
    for i in range(5):
        scores = sorted_scores[i]
        print(f"Name: {scores[0]}        Score: {scores[1]}")


scoreboard_numbers()
scoreboard_days()
scoreboard_months()
