def exponent(x, n):
    """
    get the value of n times x multiplied by itself

    :param x: number to multiply
    :param n: number of times x is multiplied
    :return: equivalent of x exponent n
    """
    result = 1
    for i in range(n):
        result *= x
    return result


# tests
print(str(exponent(5, 3)))
