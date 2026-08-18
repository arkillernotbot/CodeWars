def dir_reduc(arr):
    result = []
    opposite = {'NORTH':'SOUTH', 'SOUTH':'NORTH', 'EAST':'WEST', 'WEST':'EAST'}
​
    for direction in arr:
        if result and opposite[direction] == result[-1]:
            result.pop()
        else:
            result.append(direction)
​
    return result