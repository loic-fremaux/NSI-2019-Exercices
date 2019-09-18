def is_pair(x):
    return x % 2 == 0


# tests
number = int(input("Entrez un nombre: "))
if is_pair(number):
    print("Le nombre est pair")
else:
    print("Le nombre est impair")
