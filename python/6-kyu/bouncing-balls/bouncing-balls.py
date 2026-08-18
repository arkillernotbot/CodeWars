def bouncing_ball(h, bounce, window):
    times = 1
​
    if h > window and 0 < bounce < 1:
        while h * bounce > window:
            h = h * bounce
            times += 2
​
        return times
    else:
        return -1
    
        
        