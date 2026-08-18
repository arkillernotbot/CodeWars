def digital_root(n):
    while n > 9:
        current_sum = 0
        while n>0:
            current_sum += n%10
            n//=10
        n=current_sum
            
    return n