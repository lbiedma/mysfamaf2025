def buscar_raices_primitivas():
    """
    Busqueda de raíces primitivas de 31.
    """
    raices_primitivas = []
    for a in range(1, 31):
        if a**15 % 31 == 1:
            continue
        if a**10 % 31 == 1:
            continue
        if a**6 % 31 == 1:
            continue
        raices_primitivas.append(a)
    
    return raices_primitivas

print(buscar_raices_primitivas())
