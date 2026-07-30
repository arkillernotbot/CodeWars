def find_short(s):
    words = s.split()
    smallest_word = len(words[0])
    for word in words[1:]:
        if len(word) < (smallest_word):
            smallest_word = len(word)
    return (smallest_word)