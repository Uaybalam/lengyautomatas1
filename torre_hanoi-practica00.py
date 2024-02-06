def TorreHanoi(n, origen, destino, aux):
    if n == 1:
        print(f'Mueve disco 1 de {origen} a {destino}')
        return
    TorreHanoi(n-1, origen, aux, destino)
    print(f'Mueve el disco {n} de {origen} a {destino}')
    TorreHanoi(n-1, aux, destino, origen)

n = 4
TorreHanoi(n, 'A', 'B', 'C')