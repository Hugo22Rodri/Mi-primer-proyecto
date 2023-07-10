print("Programa 18.\nPrograma que calcule cuanto es el interes compuesto.\n")
def interes_compuesto(Ci,i,n):
     C_F = Ci * (1 + i)**n
     return C_F

Ci = float(input("Escribe el capital inicial: "))
i = float(input("Escribe la tasa de interes: "))
n = float(input("Escribe el periodo de ahorro: "))
 
C_F = interes_compuesto(Ci,i,n)

print("El interes compuesto es ",round(C_F,2))
print("\nFin del programa")