import math
import numpy as np
from random import random
from time import time

def poisson(lamda):
    """
    Poisson sin optimizar del teorico.
    """
    U = random()
    i = 0
    p = math.exp(-lamda)
    F = p

    while U >= F:
        i += 1
        p *= lamda / i
        F = F + p

    return i

# Comienzan las funciones del ejercicio
def PY(lamb, i):
    """
    P(Y=i)
    Es la función de masa de Poisson pmf
    """
    p = math.exp(-1*lamb)
    for j in range(1, i + 1):
        p *= lamb / j

    return p

def sumatoria(lamb, k):
    """
    Constante que va en el denominador
    Es la función de distribución acumulada de una Poisson cdf
    """
    p = math.exp(-1*lamb)
    S = p
    for j in range(1, k + 1):
        p *= lamb / j
        S = S + p

    return S

def PX(lamb, k, i):
    """
    P(X=i) (i=1, ... , k)
    """
    return PY(lamb, i) / sumatoria(lamb, k)

def poisson_truncada(lamb, k):
    """
    Con Transformada Inversa
    """
    u = random()
    i = 0
    S = sumatoria(lamb, k)
    p = math.exp(-1 * lamb) / S
    F = p
    while u >= F:
        i += 1
        p *= lamb / i
        F = F + p
    return i

def poisson_truncada_mej(lamb, k):
    """
    Con Transformada Inversa Mejorada
    """
    S = sumatoria(lamb, k)
    p = math.exp(-1 * lamb) / S 
    F = p
    for j in range(int(lamb)):
        p *= lamb / j
        F += p
    j = int(lamb)
    u = random()
    if u < F:
        while u < F:
            F -= p
            p *= j / lamb
            j -= 1
        return j + 1
    else:
        while u >= F:
            j += 1
            p *= lamb / j
            F += p
        return j

def est_P(X, lamb, k, i, n_sim=100): # P(X>i)
    c = 0
    for _ in range(n_sim):
        r = X(lamb, k)
        if r > i:
            c += 1
    return c / n_sim

# ACEPTACION Y RECHAZO
def poisson_ayr(lamb, k):
    """
    Aceptación y Rechazo
    """
    y = poisson(lamb)
    u = random()
    S = sumatoria(lamb, k)
    c = 1 / S
    qy = PY(lamb, y)
    while u >= PX(lamb, k, y) / (c * qy):
        y = poisson(lamb)
        qy = PY(lamb, y)
        u = random()
    return y

def poisson_ayr_mej(lamb, k):
    while True:
        y = poisson(lamb)
        if y <= k:
            return y

print("Estimación de P(X>2) con 1000 simulaciones")
print(f"T. Inversa: {est_P(poisson_truncada, 0.7, 10, 2, n_sim=1000)}")
print(f"T. Inversa MEJORADA: {est_P(poisson_truncada_mej, 0.7, 10, 2, n_sim=1000)}" )
print("----------------------------------------------------------------------------------------")
print(f"Estimación usando Aceptación y Rechazo: {est_P(poisson_ayr, 0.7, 10, 2, n_sim=1000)}")
print(f"Método Mejorado: {est_P(poisson_ayr, 0.7, 10, 2, n_sim=1000)}")
print("----------------------------------------------------------------------------------------")
print(f"Valor exacto P(X > 2) = {1 - (PX(0.7, k=10, i=0) + PX(0.7, k=10, i=1) + PX(0.7, k=10, i=2))}")

# Si quiero comparar el tiempo de corrida de las distintas funciones de Transf Inversa
print("----------------------------------------------------------------------------------------")
start = time()
est_P(poisson_truncada, 0.7, 10, 2, n_sim=10000)
print(f"Tiempo de corrida comun: {time() - start:.5f}")
start = time()
est_P(poisson_truncada_mej, 0.7, 10, 2, n_sim=10000)
print(f"Tiempo de corrida mejorada: {time() - start:.5f}")
start = time()
est_P(poisson_ayr, 0.7, 10, 2, n_sim=10000)
print(f"Tiempo de corrida AyR: {time() - start:.5f}")
start = time()
est_P(poisson_ayr_mej, 0.7, 10, 2, n_sim=10000)
print(f"Tiempo de corrida AyR mejorada: {time() - start:.5f}")
