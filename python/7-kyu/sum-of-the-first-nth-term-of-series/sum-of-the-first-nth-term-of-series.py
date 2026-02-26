def series_sum(n):
    result = 1
    denominador = 1
    for i in range(1, n):
        denominador += 3
        result += (1 / (denominador)) 
    
    return f"{result:.2f}" if n > 0 else "0.00"