from math import log
from random import random

def poisson_homogeneo(lam, T):
    t = -log(1 - random()) / lam
    eventos = []
    while t <= T:
        eventos.append(t)
        t += -log(1 - random()) / lam
    
    return eventos, len(eventos)

def llegada_aficionados():
    _, num_buses = poisson_homogeneo(5, 1)

    aficionados = 0
    for i in range(num_buses):
        aficionados += int(21 * random() + 20)
    
    return aficionados

# esperanza = 5 (esperanza de la poisson en 1hr) * 30 (esperanza de uniforme discreta [20, 40]) = 150

numeros = []
tiradas = 10000
for i in range(tiradas):
    numeros.append(llegada_aficionados())
print(sum(numeros) / tiradas)
