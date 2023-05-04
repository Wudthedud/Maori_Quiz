def int_check(number, min, max):
    while True:
        number = input(f"Please enter a number between {min} and {max} \n")
        num = int(number)
        if min <= number <= max:
            return num
        else:
            print("The number is not between 1 and 10. Please try again.")
