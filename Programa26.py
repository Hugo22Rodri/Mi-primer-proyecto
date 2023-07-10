print('Programa 26.\nDetermina si el numero es positivo, negativo o cero.\n')
def positivo_negativo_cero(num):
    if num > 0:
         print("Es positivo")
    elif num < 0:
        print("Es negativo")
    else:
        print("Es cero")
    return num
num = float(input("Ingrese un Numero: "))
positivo_negativo_cero(num)
print("\nFin del Programa")   