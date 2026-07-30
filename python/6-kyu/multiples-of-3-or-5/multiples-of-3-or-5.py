def solution(number):
​
    if number >=0:
        total = 0
​
        for i in range (0, number):
​
            if ((i%3) == 0 or (i%5) == 0):
                total = total + i
        
        return total
​
    else:
        return 0
​