print("Programa 19.\nPrograma que calcula la compra de 5 articulos y muestra el total de la compra sin y con el impuesto.\n")
def costo_sin_impuesto(a1,e2,i3,o4,u5):
    C_S_I = a1 + e2 + i3 + o4 + u5
    return  C_S_I
def costo_con_impuesto(a1,e2,i3,o4,u5):
    C_S_I = a1 + e2 + i3 + o4 + u5
    C_C_I =  C_S_I + 0.07
    return C_C_I
def prom_de_la_com_s_impuesto(a1,e2,i3,o4,u5):
    C_S_I = a1 + e2 + i3 + o4 + u5
    C_C_I =  C_S_I + 0.07
    P_C_S_I = C_S_I / 5
    return P_C_S_I

a1 = float(input("articulo 1: "))
e2 = float(input("articulo 2: "))
i3 = float(input("articulo 3: "))
o4 = float(input("articulo 4: "))
u5 = float(input("articulo 5: "))

C_S_I = costo_sin_impuesto(a1,e2,i3,o4,u5)
C_C_I = costo_con_impuesto(a1,e2,i3,o4,u5)
P_C_S_I = prom_de_la_com_s_impuesto(a1,e2,i3,o4,u5)

print("\nEl costo sin impuesto es:",round(C_S_I,2))
print("El costo con impuesto es:",round(C_C_I,2))
print("El promedio de la compra sin impuesto es:" ,round(P_C_S_I,2))
print("\nFin del programa")