from random import randint

contador = 0
for i in range(1000000):
    X = randint(1, 6)
    if X == 1 or X == 6:
        Y = randint(1, 6)
        if 2 * Y > 6:
            contador += 1
    else:
        Y = randint(1, 6)
        Z = randint(1, 6)
        if Y + Z > 6:
            contador += 1

print(contador / 1000000)
print(5 / 9)