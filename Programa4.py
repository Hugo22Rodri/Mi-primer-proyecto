print("Programa 4. Programa que calcula el area de un triangulo\n")
def area_de_un_triangulo(B,A):
    Area = (B * A)/2
    return Area

B = Base = float(input("Escribe el valor de Base:"))
A = Altura = float(input("Escribe el valor de Altura:"))

Area = area_de_un_triangulo(B,A)
print("El area es de ", round (Area,2))
print("\nFin del programa")