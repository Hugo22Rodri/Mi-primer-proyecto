print("Programa 7.\nPrograma que calcula el volumen de un prisma rectangular.\n")
def volumen_de_un_prisma_rectangular(Largo,Ancho,Altura):
    Vol = Largo * Ancho * Altura
    return Vol

Largo = float(input("Escriba el valor de Largo: "))
Ancho = float(input("Escriba el valor de Ancho: "))
Altura = float(input("Escriba el valor de la Altura: "))

Vol = volumen_de_un_prisma_rectangular(Largo,Ancho,Altura)

print("\nEl volumen del prisma rectangular es de" ,round(Vol,2))
print("\nFin del programa")