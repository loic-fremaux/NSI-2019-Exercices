NOTES_COUNT = 3

total_notes = 0
total_coefficient = 0

i = 0
while i < NOTES_COUNT:
    # ask for last notes
    args = input("Quelles étaient tes " + str(NOTES_COUNT)
                 + " dernières notes de français ? (format: note;coefficient)").split(";")

    # add values to counts
    coefficient = float(args[1]) if len(args) > 1 else 1
    total_notes += float(args[0]) * coefficient
    total_coefficient += coefficient

    i += 1

# calculate average and round result
average = round(total_notes / total_coefficient)

print("Tu as une moyenne de " + str(average))
