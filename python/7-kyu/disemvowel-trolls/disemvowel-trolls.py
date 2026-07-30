def disemvowel(string_):
    result = ""
    for letter in string_:
        if letter not in "aAeEiIoOuU":
            result += letter
    return result