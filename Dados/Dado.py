import random
from tkinter import *

class Dado():

    #metodo constructor
    def __init__(varClase):
        varClase.numero = 1
    
    def lanzar(varClase):
        #generar al azar un azar un valor enytre 1 y 6 
        varClase.numero = random.randrange(1, 7)
    
    def obtenerNumero(varClase):
        return varClase.numero
    
    def mostrar(varClase, lbl):
        #cargar la imagen (con un objeto    photoimage)
        img = PhotoImage(file=str(varClase.numero)+".png")
        #mostar la imagen en la etiqueta (objeto LABEL )
        lbl.config(image=img)
        lbl.imagen=img
