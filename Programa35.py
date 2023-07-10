print('Programa 35.\nMuestra los numeros del 1 al 15 y dice si es par o impar.\n')
def par_impar():
    h = 1
    while h <= 15:
        print(h)
        h += 1
        if h %2 == 0:
             print('Es un numero impar.')
        else:
             print('Es un numero par.')
par_impar()
print('\nFin del programa.')