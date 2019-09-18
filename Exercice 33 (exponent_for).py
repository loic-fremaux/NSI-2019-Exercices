def exponent(x, n):
    x_value = x
    for i in range(n - 1):
        x *= x_value
    return x


# tests
assert exponent(5, 3) == 125
