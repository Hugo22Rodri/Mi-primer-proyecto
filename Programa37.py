print('Programa 37. \nToma 5 articulos y calcula el 7%.\n')
def cinco_Articulos():
    a = 0
    while a < 5:
        a += 1
        articulos = float(input('Articulo: '))
        impuesto = articulos * 0.07
        print(round(impuesto,2))
impuesto = cinco_Articulos()
print('\nFin del programa')