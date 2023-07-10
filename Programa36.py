print('Programa 36.\nMuestra que numeros del 1 al 10 son mayor, menor o igual que cinco.\n')
def mayor_menor_igual_a_5():
    for num in range(1,11):
        if num> 9:
            break 
        elif num > 5:
            print(f'{num} mayor a 5')
        elif num < 5:
            print(f'{num} menor a 5')
        elif num <= 5:
            print(f'{num} menor igual a 5')
        else:
            print(f'{num} Es cero')
mayor_menor_igual_a_5()
print('\nFin del programa\n')