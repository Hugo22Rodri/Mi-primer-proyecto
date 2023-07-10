print("Programa 20.\nPrograma que calcula los salarios netos de empleados.\n")
def salarios_netos_de_empleados(S_B):
    S_S = S_B * 0.08
    S_E = S_B * 0.02
    I = S_B * 0.15
    P = 100
    S_N = S_B - S_S - S_E - I - P
    return   S_N
S_B = float(input("Escribe el valor del salario bruto: "))
S_N = salarios_netos_de_empleados(S_B)
print("El salario neto es:" , S_N)
print("\nFin del programa")