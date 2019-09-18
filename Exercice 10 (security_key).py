code = int(input("Quel est votre code de sécurité sociale ?"))

key = 97 - (code % 97)

print("Votre clé de sécurité est " + str(key))
