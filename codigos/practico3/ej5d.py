from math import exp, pi, sqrt
from random import random

# La integral entre -inf e inf de e^(-x^2) = 2 integral entre 0 e inf de e^(-x^2)
# La integral entre 0 e inf de e^(-x^2) = sqrt(pi)/2

def integral_montecarlo_0_inf(funcion, N):
    suma = 0
    for i in range(N):
        U = random()
        suma += funcion(1/U - 1) / U**2
    
    return suma / N

def fun(x):
    return exp(-x**2)

for N in [1000, 5000, 10000]:
    aprox = 2 * integral_montecarlo_0_inf(fun, N)
    print(f"aproximacion para {N} = {aprox}")
    print(f"error absoluto = {abs(sqrt(pi) - aprox)}")
