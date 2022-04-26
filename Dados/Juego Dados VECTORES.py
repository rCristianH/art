from tkinter import *
import Util
from classDado import Dado

#crear ventana
v = Tk()
v.title("Juego de Dados")

#Imagenes de los dados

totalDados=10
lblDado=[]
for i in range(0, totalDados):
    lblDado.append(Util.agregarImagen(v, "1.png", 0, i))

#Etiquetas
Label(v, text="Lanzamientos").grid(row=2, column=0)
Label(v, text="Cenas").grid(row=2, column=1)
#Cajas de texto para mostrar estado de los lanzamientos
txtLanzamientos=Util.agregarCajaTextoSalida(v, 3, 3, 0, "Arial 48 bold")
txtCenas=Util.agregarCajaTextoSalida(v, 3, 3, 1, "Arial 48 bold")

#crear las instancias de los dados
dados = []
for i in range(0, totalDados):
    dados.append(Dado())

lanzamientos = 0
cenas = 0
Util.mostrarCajaTexto(txtLanzamientos, lanzamientos)
Util.mostrarCajaTexto(txtCenas, cenas)

def lanzarDados():
    global lanzamientos, cenas
    #lanzar los 2 dados
    for i in range(0, len(dados)):
        dados[i].lanzar()

        #mostrar los dados
        dados[i].mostrar(lblDado[i])

    #administrar contadores
    lanzamientos += 1
    Util.mostrarCajaTexto(txtLanzamientos, lanzamientos)
    if dados[0].obtenerNumero() + dados[1].obtenerNumero() >= 11:
        cenas += 1
        Util.mostrarCajaTexto(txtCenas, cenas)

Button(v, text="Lanzar", command=lanzarDados).grid(row=1, column=0)



