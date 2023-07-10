print("Programa 13.\nPrograma que calcula el salario neto.\n")
def salario_neto():
    S_S = S_b * 0.0514
    S_E = S_b * 0.02
    P = 50

    S_Neto = S_b - S_S - S_E - P
    return S_Neto
    
S_b = float(input("Escribe el valor del salario bruto: "))
S_Neto = salario_neto()
print("El salario neto es: ",S_Neto)
print("\nFin del programa")