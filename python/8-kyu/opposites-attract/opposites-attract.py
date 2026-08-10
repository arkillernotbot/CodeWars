def lovefunc( flower1, flower2 ):
    if flower1%2==0:
        return flower2%2==1
    if flower2%2==0:
        return flower1%2==1
    else:
        return False