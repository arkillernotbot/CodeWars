def find_uniq(arr):
    counts = {}
​
    for i in arr:
        counts[i] = counts.get(i, 0) + 1
​
    for i in counts:
        if counts[i] == 1:
            return i