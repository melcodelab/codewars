def descending_order(num: int) -> int:
    """
    Receives a positive integer and rearranges its digits in descending order to return the largest possible number. 
    Example: 
        Input: 42145 -> Output: 54421
        Input: 0 -> Output: 0
    """
    digits = sorted(str(num), reverse=True)
    return int("".join(digits)) if num > 0 else 0
    
    