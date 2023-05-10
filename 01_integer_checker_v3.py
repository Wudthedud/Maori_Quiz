def int_check(question, minimum, maximum):
    while True:
        number = input(question)
        num = int(number)
        if minimum <= number <= maximum:
            return num
        else:
            print(f"The number is not between {min} and {max}. Please try again.")


