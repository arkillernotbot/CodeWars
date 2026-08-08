def is_valid_walk(walk):
    x = 0
    y = 0
    if len(walk) == 10:
        for direction in walk:
            if direction == 'n':
                x += 1
            if direction == 's':
                x -= 1
            if direction == 'e':
                y += 1
            if direction == 'w':
                y -= 1
        if x == 0 and y == 0:
            return True
        else:
            return False
        
    else:
        return False