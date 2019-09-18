def minmax(*numbers):
    mini = None
    maxi = None
    for number in numbers:
        if mini is None or number < mini:
            mini = number
        if maxi is None or number > maxi:
            maxi = number

    return [mini, maxi]


# tests
results = minmax(8, -2, 4)
print("Le nombre le plus petit est " + str(results[0]) + ", le nombre le plus grand est " + str(results[1]))
