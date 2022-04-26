#Importar la libreria para GUI
from tkinter import *
#Importar funcionalidad CAJA DE MENSAJES
from tkinter import messagebox
import re
import math

#Instancia la ventana principal de la aplicacion
ventana = Tk()

#Asigna el titulo de la ventana
ventana.title("Funcion Seno")

Label(ventana, text="Terminos de la serie").grid(row=0)
txtN= Entry(ventana, width=10)
txtN.grid(row=0, column=1)

Label(ventana, text="Angulo (grados)").grid(row=1)
txtA= Entry(ventana, width=10)
txtA.grid(row=1, column=1)

txtS = Entry(ventana, width=20)
txtS.grid(row=2, column=1)
txtS.configure(state=DISABLED)

txtSR = Entry(ventana, width=20)
txtSR.grid(row=3, column=1)
txtSR.configure(state=DISABLED)

def gradosARadianes(grados):
    return grados * math.pi / 180

def factorial(x):
    f = 1
    for j in range(2, x+1):
        f *= j
    return f

def calcularSeno():
    if re.match("^[-]?[0-9]+[.]?[0-9]*$", txtA.get()) and \
        re.match("^[0-9]+$", txtN.get()):

        n=int(txtN.get())
        a=float(txtA.get())

        #proceso
        #Convetir de grados a radianes
        x = gradosARadianes(a)
        s = 0
        for i in range(0,n+1):
            #Calcular el factorial de 2 * i + 1
            p = 2 * i + 1
            f = factorial(p)

            #Calcular el término y acumularlo
            s = s + (-1)** i / f * x ** p

        txtS.configure(state=NORMAL)
        txtS.delete(0, END)
        txtS.insert(0, "{0:,.12f}".format(s))
        txtS.configure(state=DISABLED)

        txtSR.configure(state=NORMAL)
        txtSR.delete(0, END)
        txtSR.insert(0, "{0:,.12f}".format(math.sin(x)))
        txtSR.configure(state=DISABLED)

    else:
        messagebox.showerror("", "Datos no validos")

Button(ventana, text="Calcular", command=calcularSeno).grid(row=2)




