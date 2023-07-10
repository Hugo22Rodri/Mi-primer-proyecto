print("Programa 10.\nPrograma que convierte una unidad de metros a pies y a pulgadas.\n")
def metros_a_pies(metros):
    Pies = metros * 3.28 
    return Pies
metros = int(input("Escribe el valor de metros a convertir: "))
ft = metros_a_pies(metros)
print('metros a pies:',ft)

def metros_a_pulgadas(metros):
    Pulgadas = metros * 39.37
    return Pulgadas
metros = int(input("Escribe el valor de metros a convertir: "))
In = metros_a_pulgadas(metros)
print('metros a pulgadas:',In)

print("\nFin del programa")