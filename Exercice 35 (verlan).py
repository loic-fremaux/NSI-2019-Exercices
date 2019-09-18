def verlan(string):
    """
    invert the content of a string

    :param string: to invert
    :return: inverted string
    """
    result = ""
    length = len(string)
    for i in range(1, length + 1):
        result += string[length - i]
    return result


# tests
word = input("Entrez un mot: ")
print(verlan(word))
