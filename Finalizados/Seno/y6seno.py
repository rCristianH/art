import math
print("Programa para calcular el seno de un angulo e grados")

def convertirARadianes(angulo):
    return angulo * math.pi / 180

def obtenerFactorial(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f

try:
    a = float(input("Angulo en (grados)? "))
    n = int(input("Total de terminos? "))

    if n>0:

        x = convertirARadianes(a)
        s = 0
        for i in range(0, n+1):
            p = 2*i + 1
            t = (-1)**i / obtenerFactorial(p) * x**p
            s += t

        print("El valor del seno es ", "{0:,.12f}".format(s))
        print("El valor real del seno es ", "{0:,.12f}".format(math.sin(x)))
    else:
        print("El total de terminos debe ser mayor a 0")
except:
    print("Error en la entrada de datos")