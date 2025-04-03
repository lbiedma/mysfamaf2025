import matplotlib.pyplot as plt

def generador_nuevo(a, c):
    """
    Generador de números pseudoaleatorios utilizando un generador lineal congruencial
    Pueden cambiar y x por cualquier semilla que se les ocurra
    """
    y = 1
    x = 1
    z = (y + x) % 32
    ys = [y]
    xs = [x]
    zs = [z]

    for i in range(1000):
        y = (5 * y + c) % 32
        x = (a * x) % 31
        z = (y + x) % 32
        ys.append(y)
        xs.append(x)
        zs.append(z)

    return ys, xs, zs

# Test generador_nuevo
ys, xs, zs = generador_nuevo(12, 9)

fig, ax = plt.subplots(3, 1)
ax[0].plot(ys[:-1], ys[1:], 'ro', label='y')
ax[1].plot(xs[:-1], xs[1:], 'bo', label='x')
ax[2].plot(zs[:-1], zs[1:], 'ko', label='z')
plt.show()
