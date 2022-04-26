print("Programa para convertir UCSA")

uo = int(input("Unidad Origen: 1.Barril 2.Galon 3.Cuarto 4.Pinta 5.Onza?"))

if uo == 1:
    nuo = "Barril(es)"
elif uo == 2:
    nuo = "Galon(es)"
elif uo == 3:
    nuo = "Cuarto(s)"
elif uo == 4:
    nuo = "Pinta(s)"
else:
    nuo = "Onza(s)"

co = float(input("Cantidad de "+nuo+"?"))
ud = int(input("Unidad Destino: 1.Barril 2.Galon 3.Cuarto 4.Pinta 5.Onza?"))

#validaciones
if uo in range(1, 6) and ud in range(1, 6) and \
   co >=0:

    #proceso
    #Convertir a onzas
    if uo == 1:
        #Barril
        cd = co * 2688
    elif uo == 2:
        #Galon
        cd = co * 64
    elif uo == 3:
        #Cuarto
        cd = co * 16
    elif uo == 4:
        #Pinta
        cd = co * 8
    else:
        #Onza
        cd = co

    #Convertor desde onzas a otra unidad
    nud = "Onza(s)"
    if ud == 1:
        #Barril
        cd = cd / 2688
        nud = "Barril(es)"
    elif ud == 2:
        #Galon
        cd = cd / 64
        nud = "Galon(es)"
    elif ud == 3:
        #Cuarto
        cd = cd / 16
        nud = "Cuarto(s)"
    elif ud == 4:
        #Pinta
        cd = cd / 8
        nud = "Pinta(s)"

    print(co, " ", nuo, " son ", cd, " ", nud)
else:
    print("Los datos no son válidos")
