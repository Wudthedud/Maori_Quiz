def center(string):
    whitespace = 50 - len(string)
    spaces = int(whitespace / 2)

    print(" " * spaces, end="")
    print(string, end="")
    print(" " * spaces, end="")



