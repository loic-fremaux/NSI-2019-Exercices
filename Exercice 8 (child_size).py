prefix = "Quelle est la taille de votre "
suffix = " ? (en cm)"

# get parents size
father_size = int(input(prefix + "père" + suffix))
mother_size = int(input(prefix + "mère" + suffix))

# calculate child size
parents_size = father_size + mother_size
child_boy_size = (parents_size + 13) / 2
child_girl_size = (parents_size - 13) / 2

print("Pour un garçon, la taille probable est " + str(child_boy_size) + "cm, pour une fille la taille probable est " + str(child_girl_size) + "cm.")
