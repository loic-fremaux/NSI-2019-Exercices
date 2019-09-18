def verlan(string):
    result = ""
    length = len(string)
    for i in range(length):
        result += string[length - i - 1]
    return result


def palindrome(string):
    return verlan(string) == string


# tests
word = input("Entrez un mot: ")
if palindrome(word):
    print("Ce mot est un palindrome")
else:
    print("Ce mot n'est pas un palindrome")
