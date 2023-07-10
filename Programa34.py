print("Programa 34.\nPrograma para evaluar calificaciones.")
def evaluciones():
    G = 5
    for G in range(G):
        e_1 = int(input(f'Ingrese su calificacion {G + 1}: '))
        if e_1 >= 90:
            print("A")
        elif e_1 >= 80 <= 89:
            print("B")
        elif e_1 >= 70 <= 79:
            print("C")
        elif e_1 >= 60 <= 69:
            print("D")
        else:
             print("F")  
evaluciones()
print("\nFin del Programa")