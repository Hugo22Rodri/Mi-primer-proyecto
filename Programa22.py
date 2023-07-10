print('Programa 22.\nPrograma que calcula la temperatura.\n')
def calcula_tempertura(): 
    if temperature < 20: #cierto if
        if temperature <10:
          print("Nivel azul")
        else:# falso 
          print("Nivel verde")
    else:
        if temperature <30:
          print("Nivel naranja")
        else:
          print("Nivel rojo")
    return temperature
temperature = float(input("Escriba la temperatura: ")) 
tem = calcula_tempertura()
print(tem)

print(" \nFin del programa\n")