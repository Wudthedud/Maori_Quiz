""""
TO DO

 5. Provide feedback after each round, find a way to make questions look better instead of block of text 
 6. Format the text/make responses and questions look better 
 2. Divide functions into classes (time dependent)
"""""
# Make a specific word centered - highscore pull and string formatter still doens't center the string and names
#  3. Create quiz for days of the week, easy - ask for numbers, medium - ask for day with names, hard - multi choice
#  4. Finish main program, add option to retry the game, ask if they want to see the scoreboard
import shelve

d = shelve.open('score.txt')
numbers_highscore = d['highscores_numbers']
days_highscore = d['highscores_days']
months_highscore = d['highscores_months']
d.close()

print(numbers_highscore)
print(days_highscore)
print(months_highscore)