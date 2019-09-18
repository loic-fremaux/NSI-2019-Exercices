n = int(input("Entrez un nombre entre 1 et 10: "))
u = 1
v = 1

for i in range(n):
    u += 2
    v *= 2
    print("Valeur de u : " + str(u))
    print("Valeur de v : " + str(v))
