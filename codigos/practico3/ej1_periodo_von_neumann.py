def periodo_von_neumann(x):
    contador = 1
    lista_generada = [x]
    for i in range(10000):
        x = (x**2 // 100) % 10000
        if x in lista_generada:
            break
        lista_generada.append(x)
        contador += 1
    
    return contador

print(periodo_von_neumann(3009))
print("------------------------")
print(periodo_von_neumann(7600))
print("------------------------")
print(periodo_von_neumann(1234))
print("------------------------")
print(periodo_von_neumann(4321))
