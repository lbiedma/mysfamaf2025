import matplotlib.pyplot as plt
import math

def randu(a, M):
    x = 1
    lista = [x]
    for i in range(50000):
        x = (a * x) % M
        lista.append(x)
    
    return lista

a = 2**16+3 #7**5
M = 2**31 # 2 ** 31 - 1
lista = randu(a, M)

xs = lista[0::3]
ys = lista[1::3]
zs = lista[2::3]

# Plot 3D de los puntos generados con ternas (u_i, u_i+1, u_i+2)
# Rotarlo para encontrar los hiperplanos
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs, c='r', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# Estimacion de puntos que entran en una esfera de radio M/10
# en el cubo de lado 
# Esto deberia darnos cercano a el cociente volumen de la esfera / volumen del cubo
contador = 0
for i in range(0, int(50001 / 3)):
    if (xs[i] - M / 2)**2 + (ys[i] - M / 2)**2 + (zs[i] - M / 2)**2 <= (M / 10)**2:
        contador += 1

print(f"Estimacion de puntos en la esfera: {contador / (50001 / 3)}")
print(4 * math.pi / 3000)


