def string_checker(question_, minimum, maximum):
    while True:
        string = input(f"{question_} \n").strip()
        if not string.isalpha():
            print("Please only input characters (A-Z)")
        elif len(string) < minimum or len(string) > maximum:
            print(f"Please make sure your text is between {minimum} and {maximum} characters long")
        else:
            return string
