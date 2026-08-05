def expanded_form(num):
    l = []
    num = str(num)
    num =list(num[::-1])
    for index, digit in enumerate(num):
        if digit != "0":
            digit = digit + "0"*index
            l.append(digit)
    l.reverse()
    return " + ".join(l)
​