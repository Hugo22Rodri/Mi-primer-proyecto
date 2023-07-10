print('Programa 24.\ncalculadora de descuentos.\n')
def calculadora_de_descuentos(c1,c2):
    precio_final = c1 - (c1 * c2/100)
    return precio_final

c1 = float(input("Escribe el precio: "))
c2 = float(input("Escribe el descuento: "))

precio_final = calculadora_de_descuentos(c1,c2)

print("El precio final es:",precio_final)
if precio_final < 50:
    print("\n¡Oferta Especial!")
print("\nFin del programa.")