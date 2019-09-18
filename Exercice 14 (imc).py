weight = int(input("Entrez votre poids en kg: "))
sqrdSize = float(input("Entrez votre taille en m: ")) ** 2

if weight / sqrdSize > 25:
    print("Vous êtes en surpoids")
elif weight / sqrdSize < 18.5:
    print("Vous êtes trop maigre")
else:
    print("Vous avez une corpulence normale")
