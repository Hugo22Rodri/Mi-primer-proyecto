print("Programa 16.\nPrograma que calcula la nota final.\n")
def nota_final(a1,a2,a3,a4,a5):
    S_N = (a1 + a2 + a3 + a4 + a5) / 5
    Pesos = (0.20 + 0.15 + 0.25 + 0.10 + 0.30)
    Nota_final= S_N * Pesos
    return Nota_final

a1 = float(input("Escriba el valor de evaluacion1: "))
a2 = float(input("Escriba el valor de evaluacion2: "))
a3 = float(input("Escriba el valor de evaluacion3: "))
a4 = float(input("Escriba el valor de evaluacion4: "))
a5 = float(input("Escriba el valor de evaluacion5: "))

r = nota_final(a1,a2,a3,a4,a5)
print('Tu nota final es:',r)