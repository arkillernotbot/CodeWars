def find_it(seq):
    return next(number for number in seq if seq.count(number) % 2)