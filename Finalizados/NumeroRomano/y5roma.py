print("Programa para convertir numeros Enteros a Romanos")


try:
    na = int(input("Ingrese el numero que desea convertir: "))
    if na>0 and na<4000:
        romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "X", "V", "IV", "I"]
        valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        nai = na 
        r = ""
        p = 0
        while na > 0:
            while na < valores [p]:
                p += 1
            na -= valores[p]
            r += romanos[p]
        
        print("En mumero romano para", nai, "es", r)

    else:
        print("Dato no valido (Numeros enteros entre 1 y 3999)")
except Exception as e:
    print("Error en la entrada de datos\n[", e, "]")


