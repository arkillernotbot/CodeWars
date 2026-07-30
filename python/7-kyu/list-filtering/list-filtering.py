def filter_list(l):
    filtered = []
    for num in l:
        if isinstance(num, int):
            filtered.append(num)
    return filtered