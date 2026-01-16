def digitize(n: int) -> list[int]:
    """
    Receives a non-negative integer and returns a list of its digits in reverse order.
    Example: 
        35231 => [1,3,2,5,3]
        0     => [0]
    """
    
    if n == 0:
        return [0]
    else:
        numbers = str(n)[::-1]
        list_organize = [ int(number) for number in numbers ]
        return list_organize