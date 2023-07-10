print("\nPrograma 2.\n")
def valores_de_A_B_AUX():
    A = 10
    B = 20
    AUX = A
    A = B
    B = AUX
    return A,B,AUX

V1 = valores_de_A_B_AUX()
print("valores de A , B , AUX:",V1)
print("\nFin del programa")