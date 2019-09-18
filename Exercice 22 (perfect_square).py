from math import sqrt


def is_perfect_square(x):
    return sqrt(x) % 1 == 0


# tests
number = int(input("Entrez un nombre: "))
if is_perfect_square(number):
    print("Ce nombre est un carré parfait")
else:
    print("Ce nombre n'est pas un carré parfait")
