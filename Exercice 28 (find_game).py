from random import randint

toGuess = randint(1, 100)
attempts = 0

while attempts < 8:
    number = int(input("Devinez le nombre: "))
    if number < toGuess:
        print("Le nombre à trouver est plus grand")
    elif number > toGuess:
        print("Le nombre à trouver est plus petit")
    else:
        exit("Bravo ! Tu as trouvé le nombre")
        # or
        # print("Bravo ! Tu as trouvé le nombre")
        # break
    attempts += 1

print("Tu n'as pas trouvé le nombre... il fallait deviner " + str(toGuess) + " !")
