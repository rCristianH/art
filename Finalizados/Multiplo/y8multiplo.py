print("Programa para calcular suma de multiplos de un numero")

m = int(input("Multiplos de ?"))
n = int(input("Tope de la suma?"))

if m > 0 and n >=m:
    #proceso

    s = 0
    for i in range(m, n+1, m):
        s += i

    #s = 0
    #for i in range(1, n+1):
    #    if i % m == 0:
    #        s += i

    print("la sumatoria es ", "{0:,.0f}".format(s))
    
else:
    print("Los datos no son validos")
