print("Programa 8.\nPrograma que resuelve ecuaciones lineales.\n")
def ecuaciones_1(x):
    A = 20 -(7*x)
    return A
def ecuaciones_2(x):
    B = -(7*x)+2-(10*x)+5
    return B
def ecuaciones_3(x):
    C = (4*x)+4+(9*x)+18
    return C
def ecuaciones_4(x):
    D = (6*x)-5-(8*x)+2
    return D
def ecuaciones_5(x):
    E = ((5*x)+78)/28
    return E
def ecuaciones_6(x):
    F =(((6*x)-7)/4)+(((3*x)-5)/7)
    return F

x = int(input("Escribe el valor de x: "))
a = ecuaciones_1(x)
b = ecuaciones_2(x)
c = ecuaciones_3(x)
d = ecuaciones_4(x)
e = ecuaciones_5(x)
f = ecuaciones_6(x)

print('a:',round(a,2))
print('b:',round(b,2))
print('c:',round(c,2))
print('d:',round(d,2))
print('e:',round(e,2))
print('f:',round(f,2))

print("\nFin del programa")