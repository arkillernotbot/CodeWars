def two_sum(numbers, target):
    for i, number1 in enumerate(numbers):
        for j in range(i+1, len(numbers)):
            if number1 + numbers[j] == target:
                return(i,j)