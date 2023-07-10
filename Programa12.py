print("Programa 12.\nPrograma que calcula el interes a pagar por un prestamo.\n")
def cuota(t,m,p):
    t_p= t * 100 
    t_m= t / 12
    c = m*(t_m/(1 -(1 + t_m)**(-p)))
    return c
def interes_mensual(t,m,p):
    t_p= t * 100 
    t_m= t / 12
    c = m*(t_m/(1 -(1 + t_m)**(-p)))
    i_m = m * t_m
    return i_m
def capital_mensual(t,m,p):
    t_p= t * 100 
    t_m= t / 12
    c = m*(t_m/(1 -(1 + t_m)**(-p)))
    i_m = m * t_m
    c_m = c - i_m
    return c_m

m = float(input("Escribe el valor de monto: "))
t = float(input("Escribe el valor de tasa: "))
p = float(input("Escribe el valor de plazo: "))
c = cuota(t,m,p)
i_m = interes_mensual(t,m,p)
c_m = capital_mensual(t,m,p)

print("\nla cuota es ", round(c,2))
print("El interes_mensual es ", round(i_m,2))
print("El capital_mensual es ", round(c_m,2))
print("\nFin del programa")