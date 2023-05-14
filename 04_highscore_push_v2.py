import shelve

d = shelve.open('score.txt')  # here you will save the score variable
d['highscores_numbers'] = [["Numbers_User1", 10], ["Numbers_User2", 9], ["Numbers_User3", 8], ["Numbers_User4", 7],
                           ["Numbers_User5", 6]]
d['highscores_days'] = [["Days_User1", 10], ["Days_User2", 9], ["Days_User3", 8], ["Days_User4", 7], ["Days_User5", 6]]
d['highscores_months'] = [["Months_User1", 10], ["Months_User2", 9], ["Months_User3", 8], ["Months_User4", 7],
                          ["Months_User5", 6]]

d.close()

