print('Programa 39.\nCalcula la suma de los numeros pares entre 1 al 20.\n')
def funcion_sumar_numeros_pares(n):
    s = 0
    for u in range(1,n + 1):
        if u % 2 == 0:
            s += u     
    return s

s_p = funcion_sumar_numeros_pares(20)
print('La suma de los pares es de:',s_p)