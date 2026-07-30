def square_digits(num):
    num = str(num)
    result = ""
    for i in num:
        i = int(i)
        a = i*i
        a = str(a)
        result += a
        
    result = int(result)
    return result