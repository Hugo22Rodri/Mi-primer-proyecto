print("Programa 17.\nPrograma que convierte de una unidad de medida a otra.\n")
def convertir_de_kg_a_g(kilogramos):
    g = kilogramos * 1000
    return g
kilogramos = float(input("convertir de kilogramos a gramos: "))
def convertir_de_g_a_kg(gramos):
    kg = gramos * 0.0001
    return kg
gramos = float(input("convertir de gramos a kilogramos:"))
def convertir_de_m_a_cm(metros):
    cm = metros * 100
    return cm
metros = float(input("convertir de metros a centimetros:"))
def convertir_de_cm_a_m(centimetros):
    m =  centimetros / 100
    return m
centimetros = float(input("convertir de centimetros a metros:" ))

g = convertir_de_kg_a_g(kilogramos)
kg = convertir_de_g_a_kg(gramos)
cm = convertir_de_m_a_cm(metros)
m = convertir_de_cm_a_m(centimetros)

print('\nkilogramos a gramos:',g)
print('gramos a kilogramos:',kg)
print('metros a centimetros:',cm)
print('cmntimetros a metros:',m)

print("\nFin del programa")