print("Programa 9.\nPrograma que resuelve ecuaciones.\n")
def ecuacion_m(a,b):
    C1 = (4 * a) + (3 * b)
    return C1
def ecuacion_n(a,b):
    C2 = (21 * a) - 18 + (8 * b) - 5
    return C2
def ecuacion_o(a,b):
    C3 = (4 * a) + (3 * b) +7
    return C3
def ecuacion_p(a,b,c):
    C5 = (2 * a) + (3 * b) - c**5
    return C5
def ecuacion_q(a,b,c):
    C6 = (2 * a) + (3 * b)/ - c**2
    return C6
a = int(input("Escriba el valor de a: "))
b = int(input("Escriba el valor de b: "))
c = int(input("Escriba el valor de c: "))
C1 = ecuacion_m(a,b)
C2 = ecuacion_n(a,b)
C3 = ecuacion_o(a,b)
C5 = ecuacion_p(a,b,c)
C6 = ecuacion_q(a,b,c)    
print("\nproblema I ",round(C1,2))
print("problema II ",round(C2,2))
print("problema III ",round(C3,2))
print("problema IV ",round(C5,2))
print("problema V ",round(C6,2))
print("\nFin del progroma")