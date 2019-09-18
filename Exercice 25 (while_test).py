a = 100
b = 0
i = 0

while a > b:
    i += 1
    a -= i
    a = b + i ** 2

print(i)
