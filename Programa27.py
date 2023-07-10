print("\nPrograma 27.\nEvaluador de calificaciones.\n")
def notas_de_la_U():
    if e_1 >= 90:
        print('A')
    elif e_1 >= 80 <= 89:
        print('B')
    elif e_1 >= 70 <= 79:
        print('C')
    elif e_1 >= 60 <= 69:
        print('D')
    else:
        print('F')
    return e_1
e_1 = float(input("Ingrese su calificacion: "))
        
notas_de_la_U()
print("\nFin del Programa")