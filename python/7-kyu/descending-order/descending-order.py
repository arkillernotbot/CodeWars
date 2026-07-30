def descending_order(num):
    l = list(str(num))
    l.sort(reverse=True)
    return (int("".join(l)))
​
    