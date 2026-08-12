def high(x):
    words = x.split()
    return max(words, key=lambda word:sum(ord(letter)- ord('a') + 1 for letter in word))