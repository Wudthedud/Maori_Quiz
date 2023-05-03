def yes_no(question):
    while True:
        answer = input(question + " (Y/N): \n").strip().lower()
        if answer == "yes" or answer == "y":
            return True
        elif answer == "no" or answer == "n":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'")
