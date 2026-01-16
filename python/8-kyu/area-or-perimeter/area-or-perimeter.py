def area_or_perimeter(l: int, w: int) -> int | None:
    """
    Calculate the square area or rectangle perimeter.
    
    Args:
        l (int): is length
        w (int): is width
    
    Returns: 
        l * w (int): If it is a square, return its area. 
        (2 * l) + (2 * w) (int): If it is a rectangle, return its perimeter.
    """
    
    if l == w:
        return l * w
    else:
        return (2 * l) + (2 * w)