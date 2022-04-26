print("Programa para convertir de numeros decimales a binarios")

try:
    nd = int(input("Número decimal?"))

    if nd >=0:

        nb = ""
        while nd > 1:
            db = nd % 2
            nb = str(db) + nb
            nd = nd // 2

        nb = str(nd) + nb

        print("El numero binario es ", nb)
        
    else:
        print("Digite un número entero mayor o igual a cero")

except:
    print("Error en la entrada de datos")