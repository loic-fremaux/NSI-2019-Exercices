tests = [2, 3, 5, 10]

number = int(input("Entrez un nombre: "))

divisibles = ""
non_divisibles = ""

for i in tests:
    if number % i == 0:
        divisibles += str(i) + ", "
    else:
        non_divisibles += str(i) + ", "

divisibles = divisibles[:-2]
non_divisibles = non_divisibles[:-2]

print(str(number) + " n'est pas divisible par " + non_divisibles)
print(str(number) + " est divisible par " + divisibles)
