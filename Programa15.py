print("Programa 15.\nprograma que permite ingresar 3 precios y dar el total con el impuesto.\n")
def calculador_de_impuesto_de_3_precios(A1,A2,A3):
    C_S_I = (A1 + A2 + A2)
    C_I = C_S_I * 0.07
    C_T = C_S_I + C_I
    return C_T

A1 = float(input("Escribe el valor del primer articulo: "))
A2 = float(input("Escribe el valor del segundo articulo: "))
A3 = float(input("Escribe el valor del tercer articulo: "))

C_T = calculador_de_impuesto_de_3_precios(A1,A2,A3)

print("El resultado de la compra es ",round(C_T,2))
print("\nFin del programa")