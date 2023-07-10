print("Programa 30.\nEvaluacion de calificaciones.\n")
def evaluacion_universitaria():
    b = 0
    while b < 5:
        cl = float(input("Ingrese su calificacion: "))
        if cl >= 90:
            print("A")
        elif cl >= 80 <= 89:
            print("B")
        elif cl >= 70 <= 79:
            print("C")
        elif cl >= 60 <= 69:
            print("D")
        else:
            print("F")    
        b += 1
evaluacion_universitaria()
print('\nFin del programa')