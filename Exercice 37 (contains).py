def contains(string, char):
    occurrences = 0
    for i in range(len(string)):
        if string[i] == char:
            occurrences += 1
    return occurrences


# tests
sentence = input("Entrez un mot: ")
charToFind = input("Entrez un caractère: ")
print("\"" + sentence + "\" contient " + str(contains(sentence, charToFind)) + " fois le caractère " + charToFind)
