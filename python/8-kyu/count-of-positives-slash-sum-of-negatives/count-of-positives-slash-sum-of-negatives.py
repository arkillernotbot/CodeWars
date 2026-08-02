def count_positives_sum_negatives(arr):
    positive = 0
    negative = 0
    if not arr:
        return []
    for number in arr:
        if number>0:
            positive += 1
        else:
            negative += number
    return [positive,negative]