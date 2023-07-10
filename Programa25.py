print('Programa 25.\nCalcula que tipo de triangulo es.')
def tipos_de_triangulos():
    T = 0
    while T < 3:
        l1 = float(input("Escriba el primer lado: "))
        l2 = float(input("Escriba el segundo lado: "))
        l3 = float(input("Escriba el tecer lado: "))
        
        if  l1 == l2 == l3: 
                 print("\nEs un triagulo equilatero\n ")
        if  l1 == l2 != l3: 
                print("\nEs un triagulo isosceles\n")
        if  l1 != l2 != l3: 
                print("\nEs un triagulo escaleno\n")
        T +=1
tipos_de_triangulos()
print(" \nFin del programa.\n")