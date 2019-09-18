from random import randint

toGuess = randint(0, 10)
number = int(input("Entrez un nombre: "))

if toGuess == number:
    print("Vous avez gagné !")
else:
    print("Vous avez perdu !")
