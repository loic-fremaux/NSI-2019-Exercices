def verlan(string):
    result = ""
    length = len(string)
    for i in range(length):
        result += string[length - i - 1]
    return result


# tests
word = input("Entrez un mot: ")
print(verlan(word))
