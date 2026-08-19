def capitals(word):
    return [index for index, character in enumerate(word) if character.isupper() and not character.isdigit()]