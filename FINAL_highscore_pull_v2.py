import shelve


# Prints the scoreboard with some formatting so that it looks bettwe
def scoreboard():
    d = shelve.open('score.txt')
    numbers_highscore = d['highscores_numbers']
    days_highscore = d['highscores_days']
    months_highscore = d['highscores_months']
    d.close()

    print("\033[1m" + f"Numbers Quiz High Score:".center(50, " ") + "\033[0m")
    print(f"{numbers_highscore[0]} ----- {numbers_highscore[1]} points\n".center(50))

    print("\033[1m" + f"Days Quiz High Score:".center(50, " ") + "\033[0m")
    print(f"{days_highscore[0]} ----- {days_highscore[1]} points\n".center(50))

    print("\033[1m" + f"Months Quiz High Score:".center(50, " ") + "\033[0m")
    print(f"{months_highscore[0]} ----- {months_highscore[1]} points\n".center(50))
