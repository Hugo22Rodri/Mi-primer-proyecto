print('Programa 38.\nDice que numero es mayor.\n')
def numero_mayor_de_tres():
    Z = 0
    while Z < 3:
        a = int(input("\nescribe el numero: "))
        b = int(input("escribe el numero: "))
        c = int(input("escribe el numero: "))

        if  a > b and a > c:
            print("\nel numero mayor es  =" ,a)
        elif  b > a and b > c:
            print("\nel numero mayor es  =" ,b) 
        else:
            print("\nel numero mayor es =" ,c)
        Z += 1
numero_mayor_de_tres()

print('\nFin del Programa')