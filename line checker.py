def center(string):
    whitespace = 50 - len(string)
    spaces = whitespace / 2
    for i in range(int(spaces)):
        print(" ", end="")
    print(string, end="")
    for i in range(int(spaces)):
        print(" ", end="")


center("hello")