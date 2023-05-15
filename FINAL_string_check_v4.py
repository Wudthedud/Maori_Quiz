def string_checker(question_, minimum, maximum):
    loop = True
    while loop:
        string = input(f"{question_} \n").strip()
        if not string.isalpha():
            print("Please only input characters (A-Z)")
        elif len(string) < minimum or len(string) > maximum:
            print(f"Please enter text between {minimum} and {maximum} characters long")
        else:
            loop = False
            return string
