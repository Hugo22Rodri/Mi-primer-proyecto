print("Programa 14.\nPrograma que calcula el costo total de la compra de combustible.\n")
def compra_de_combustible():
    C_S_I = P_G95 * C_D_l
    C_T = C_S_I * 1.07
    return C_T

P_G95 = float(input("Escribe el precio de la gasolina_95: "))
C_D_l = float(input("Escribe  la cantidad de litros: "))

C_T = compra_de_combustible()
print("El resultado de la compra es: ",round (C_T,2))
print("\nFin del programa")