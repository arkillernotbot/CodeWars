def increment_string(string):
    index = len(string)
​
    while index > 0 and string[index - 1].isdigit():
        index -= 1
​
    number = string[index:]
​
    if number:
        return string[:index] + str(int(number) + 1).zfill(len(number))
​
    return string + '1'