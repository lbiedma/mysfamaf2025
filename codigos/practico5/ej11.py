import matplotlib.pyplot as plt
from numpy import pi, linspace
from random import random
from scipy.stats import cauchy

aux_pi = 1/pi
sqrt_aux_pi = 1/pi**(1/2)

def f_cauchy(x):
    return aux_pi * (1 / (1 + x**2))

def ej10_cauchy_metodo_razon_uniformes():
    while True:
        u = random() * sqrt_aux_pi       # --> (   0   , 1/√π )
        v = sqrt_aux_pi * (1-random()*2) # --> ( -1/√π , 1/√π )
        if u**2 < f_cauchy(v/u):         # USA f
            return v/u

lista = []
N = 10000
for i in range(N):
    valor = ej10_cauchy_metodo_razon_uniformes()
    lista.append(max(min(valor, 5), -5))

x = linspace(-5, 5, 301)
pdf = cauchy(loc=0, scale=1).pdf(x)

plt.xlim(-5, 5)
plt.hist(lista, bins=101, density=True)
plt.plot(x, pdf)
plt.show()
