import random
from tkinter import Label, PhotoImage

#importar los enumerados
from Enumerados import *

class Carta():

    #metodoconstructor
    def __init__(varClase):
        #generar # aleatorio entre 1-52
        varClase.indice = random.randrange(1, 53)

    def obtenerPinta(varClase): 
        if varClase.indice <= 13:
            return PintaCarta.TREBOL
        elif varClase.indice <= 26:
            return PintaCarta.PICA
        elif varClase.indice <= 39:
            return PintaCarta.CORAZON
        else:
            return PintaCarta.DIAMANTE
    
    def mostrar(varClase, frm, x, y):
        lbl = Label(frm)

        img = PhotoImage(file=".\Carta"+str(varClase.indice)+".gif")
        lbl.config(image=img)
        lbl.image = img
        lbl.place(x = x, y = y)

    def obtenerIndiceNumero(varClase):
        n = varClase.indice % 13
        if n == 0:
            n = 13
        return n
        
        