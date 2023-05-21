# Final version of the integer checker, checks if number, min, max, and not float
def int_check(question, minimum, maximum):
    while True:
        number = input(question)
        try:
            num = int(number)
            if minimum <= num <= maximum:
                return num
            else:
                print(f"The number is not between {minimum} and {maximum}. Please try again. \n")
        except ValueError:
            print(f"Invalid input. Please enter a whole number between {minimum} and {maximum}. \n")
