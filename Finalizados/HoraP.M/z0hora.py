print("Programa para convertir Hora regular a Hora Militar")

hora = int(input("Hora?"))
minuto = int(input("Minutos?"))
jornada = int(input("Jornada: 1.AM 2.PM ?"))

#validaciones
if hora in range(1, 13) and \
   minuto in range(0, 60) and \
   jornada in range(1, 3):

    #proceso
    horaMilitar = hora
    if jornada == 2 and hora < 12:
        horaMilitar += 12
    elif horaMilitar == 12 and jornada == 1:
        horaMilitar = 0

    print("La hora militar es ", "{1:02d}{0:02d}".format(horaMilitar, minuto))

else:
    print("Los datos no son validos")

