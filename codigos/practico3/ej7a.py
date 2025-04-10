from random import random

for N in [100, 1000, 10000, 100000, 1000000]:
    contadores = []
    for iter in range(N):
        suma = 0
        contador = 0
        while suma <= 1:
            suma += random()
            contador += 1
        contadores.append(contador)

    estimacion_esp = sum(contadores) / N
    print(f"para {N} experimentos mi aprox es {estimacion_esp}")

from math import exp
print(f"e = {exp(1)}")
