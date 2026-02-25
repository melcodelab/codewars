def is_square(n): 
    if n < 0:
        return False 
    num = n ** 0.5
    return num * num == n