def stray(arr):
    arr = sorted(arr)
    return arr[0] if arr[0] != arr[1] else arr[-1]