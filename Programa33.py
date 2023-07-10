print("Programa 33.\nPrograma que determina si el numero es positivo, negativo o cero.\n")
def positivo_negativo_cero():
    num_numeros= 5
    for s in range(num_numeros):
        num = int(input(f'Ingrese un numero_{s + 1}: '))
        if num > 0:
          print('Es positivo')
        elif num < 0:
          print('Es negativo')
        else:
          print('Es cero')
positivo_negativo_cero()

print('\nFin del programa')