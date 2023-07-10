print("Programa 23. \nprograma que dice que numero es mayor.")
def mayor_de_3_numeros(a,b,c):
    if  a > b and a > c:
        print("\nEl numero mayor es " ,a)
    if  b > a and b > c:
        print("\nEl numero mayor es " ,b)
    if  c > a and c > b:
        print("\nEl numero mayor es " ,c)
a = int(input("escribe el 1numero: "))
b = int(input("escribe el 2numero: "))
c = int(input("escribe el 3numero: "))
mayor_de_3_numeros(a,b,c)
print(" \nFin del programa\n")