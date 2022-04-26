#Importar la libreria para GUI
from tkinter import *
#Importar funcionalidad CAJA DE MENSAJES
from tkinter import messagebox
import re

#Instancia la ventana principal de la aplicacion
ventana = Tk()

#Asigna el titulo de la ventana
ventana.wm_title("Convertir a Binario")

Label(ventana, text="Numero Decimal").grid(row=0)
txtN= Entry(ventana, width=10)
txtN.grid(row=0, column=1)

txtH= Entry(ventana, width=10)
txtH.grid(row=1, column=1)
txtH.configure(state=DISABLED)
def obtenerDigitoHexadecimal(valor):
    if valor == 10:
        hexadecimal = "A"
    elif valor == 11:
        hexadecimal = "B" 
    elif valor == 12:
        hexadecimal = "C" 
    elif valor == 13:
        hexadecimal = "D" 
    elif valor == 14:
        hexadecimal = "E" 
    elif valor == 15:
        hexadecimal = "F" 
    else: 
        hexadecimal = str(valor) 
    return hexadecimal

def convertir():
    if re.match("^[0-9]+$", txtN.get()):
        n=int(txtN.get())

        #proceso
        h = ""
        while n >= 16:
            dh = n % 16
            h = obtenerDigitoHexadecimal(dh) + h
            n = n // 16 #operador // es para división entre enteros
            
        #Obtener el primer dígito con base en el último cociente
        h = obtenerDigitoHexadecimal(n) + h

        txtH.configure(state=NORMAL)
        txtH.delete(0, END)
        txtH.insert(0, h)
        txtH.configure(state=DISABLED)

    else:
        messagebox.showerror("", "Datos no validos")


Button(ventana, text="A hexadecimal", command=convertir).grid(row=1)

