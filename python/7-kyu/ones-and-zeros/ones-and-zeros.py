def binary_array_to_number(arr):
    binary = ''
    for number in arr:
        binary += str(number)
        
    return int(binary, 2)