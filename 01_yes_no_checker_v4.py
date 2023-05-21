def yes_no(question):
    while True:
        answer = input(question + " (Y/N): ").strip().lower()
        if answer == "yes" or answer == "y":
            print("Program continues")
            return True
        elif answer == "no" or answer == "n":
            print("Program continues")
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'")

