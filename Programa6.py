print("Programa 6. \n programa que calcula el area de un trapecio.\n")
def area_de_un_trapecio(Base1,Base2,Altura):
    A = (Base1 + Base2)*Altura/2
    return A

Base1 = float(input("Escriba el valor Base 1: "))
Base2 = float(input("Escriba el valor Base 2: "))
Altura = float(input("Escriba el valor de la Altura: "))

A = area_de_un_trapecio(Base1,Base2,Altura)

print("El area de un trapecio es " , round(A,2))
print("\nFin del programa")