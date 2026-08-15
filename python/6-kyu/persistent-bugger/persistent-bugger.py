import math
def persistence(n):
    count=0
    while len(str(n)) > 1:
        n = math.prod(int(digit) for digit in str(n))
        count += 1
    return count    