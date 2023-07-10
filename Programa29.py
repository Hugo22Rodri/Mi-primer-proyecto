print("\nPrograma 29.\n Determina si el numero es positivo, negativo o cero.\n")
def positive_negative_zero():
    a = 0
    while a < 4:
        num = float(input("Ingrese un Numero: "))
        if num > 0:
          print("Es positivo")
        elif num < 0:
          print("Es negativo")
        else:
          print("Es cero")
        a += 1
positive_negative_zero()
print("\nFin del Programa")