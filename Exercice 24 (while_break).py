wordToFind = "cellule"
attempt = ""

while attempt != wordToFind:
    attempt = input("Trouvez le mot: ")
    if attempt == "stop":
        print("Vous abandonnez !")
        break

print("fin")
