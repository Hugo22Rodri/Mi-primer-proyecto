print("Programa 5.\nPrograma que calcula el perimetro de un rectangulo.\n")
def perimetro_de_un_rectangulo(AB,BC,CD,DA):
    P = AB + BC + CD + DA
    return P

AB = float(input("Escriba el valor AB: "))
BC = float(input("Escriba el valor BC: "))
CD = float(input("Escriba el valor CD: "))
DA = float(input("Escriba el valor DA: "))

P = perimetro_de_un_rectangulo(AB,BC,CD,DA)

print("El perimetro del rectangulo es ", round(P,2))
print("\nFin del programa")