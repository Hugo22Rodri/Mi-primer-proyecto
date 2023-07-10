print("Programa 11.\nprograma que resuelve la regla de tres simple.\n")
def regla_de_tres(A,B,C):
    D = (B * C) / A
    return D
A = float(input("Escriba el valor de la A: "))
B = float(input("Escriba el valor de la B: "))
C = float(input("Escriba el valor de la C: "))
      
D = regla_de_tres(A,B,C)
   
print('EL resultado es :',round (D,2))
print("\nFin del programa")