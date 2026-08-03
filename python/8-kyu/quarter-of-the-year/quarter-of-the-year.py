def quarter_of(month):
    return 1 if month<=3 else (2 if 4<=month<=6 else (3 if 7<=month<=9 else 4))