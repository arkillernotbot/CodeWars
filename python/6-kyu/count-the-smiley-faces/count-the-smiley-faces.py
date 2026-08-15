def count_smileys(arr):
    count = 0
    for i in arr:
        if i in  {':)', ';)', ':D', ';D',':-D', ';-D', ':~)', ';~)', ':~D', ';~D'}:
            count += 1
    return count