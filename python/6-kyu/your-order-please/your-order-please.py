def order(sentence):
    if not sentence:
        return ''
    words = sentence.split()
    result = [""] * len(words)
    for word in words:
        for char in word:
            if char.isdigit():
                position = int(char)
                result[position - 1] = word
    return " ".join(result)