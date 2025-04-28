from random import random
from time import time

urna_lista = [11, 14, 9, 8, 12, 10, 9, 7, 11, 9]
urna = []
for ind in range(len(urna_lista)):
    urna += urna_lista[ind] * [ind + 1]

def metodo_urna(urna):
    i = int(random() * len(urna))
    return urna[i]

start = time()
for i in range(1000000):
    metodo_urna(urna)
final_time = time() - start

print(final_time)
