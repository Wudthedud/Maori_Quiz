def string_checker(string):
    if len(string) == 0:
        return False
    elif not string.isalpha():
        return False
    else:
        return True

