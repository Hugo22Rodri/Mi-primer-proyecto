print('Programa 31 \nDetermina si eres mayor o menor de edad.\n')
def menores_o_mayores_de_edad():
    continuar = 0
    while continuar < 4:
        edad = int(input('\nIngresar su edad: '))
        if edad >= 18:
            print('Eres mayor de edad')
        else:
            print('Aun eres menor de edad')
        continuar += 1
menores_o_mayores_de_edad()
print('\nHasta luego...')