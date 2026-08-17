def how_much_i_love_you(nb_petals):
    petals = {
        1:"I love you",
        2:"a little",
        3:"a lot",
        4:"passionately",
        5:"madly",
        6:"not at all"
    }
    while nb_petals > 6:
        nb_petals -=6
    return petals.get(nb_petals)