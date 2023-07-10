print('Programa 21.\nCalcula si una persona paga impuesto.\n')
def paga_de_impuesto():
    if salario <= 3000:
        impuesto = salario * 1.07
        print("Esta debe abonar un impuesto de ", impuesto)
    else:
        print("No debe abonar impuestos")
        return salario
salario = float(input("Escriba el salario: "))
paga_de_impuesto()
print(" \nFin del programa")