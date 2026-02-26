def series_sum(n):
    return f"{sum(1 / i for i in range(1, n * 3, 3)):.2f}" if n > 0 else "0.00"
    