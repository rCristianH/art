print("Programa para convertir a hexadecimal")

#subprograma
def obtenerDigitoHex(valorDecimal):
    if valorDecimal == 10:
        digitoHex = "A" 
    elif valorDecimal == 11:
        digitoHex = "B" 
    elif valorDecimal == 12:
        digitoHex = "C" 
    elif valorDecimal == 13:
        digitoHex = "D" 
    elif valorDecimal == 14:
        digitoHex = "E" 
    elif valorDecimal == 15:
        digitoHex = "F" 
    else: 
        digitoHex = str(valorDecimal)
    return digitoHex
    
try:
    n=int(input("Número Decimal?"))
    if n >=0:
        #proceso
        h = ""
        while n > 15:
            dh = n % 16
            h = obtenerDigitoHex(dh) + h
            n = n // 16 #operador // es para división entre enteros
                
        #Obtener el primer dígito con base en el último cociente
        h = obtenerDigitoHex(n) + h

        print("El valor Hexadecimal es ", h)
    else:
        print("Digite un número entero mayor o igual a cero")
except:
    print("Error en la entrada de datos\n")

