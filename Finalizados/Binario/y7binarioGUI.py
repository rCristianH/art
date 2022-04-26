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

def convertir():
    if re.match("^[0-9]+$", txtN.get()):
        n=int(txtN.get())

        #proceso
        h = ""
        while n >= 16:
            dh = n % 16
            if dh == 10:
                h = "A" + h
            elif dh == 11:
                h = "B" + h
            elif dh == 12:
                h = "C" + h
            elif dh == 13:
                h = "D" + h
            elif dh == 14:
                h = "E" + h
            elif dh == 15:
                h = "F" + h
            else: 
                h = str(dh) + h
            n = n // 16
        if n == 10:
            h = "A" + h
        elif n == 11:
            h = "B" + h
        elif n == 12:
            h = "C" + h
        elif n == 13:
            h = "D" + h
        elif n == 14:
            h = "E" + h
        elif n == 15:
            h = "F" + h
        else: 
            h = str(n) + h

        txtH.configure(state=NORMAL)
        txtH.delete(0, END)
        txtH.insert(0, h)
        txtH.configure(state=DISABLED)

    else:
        messagebox.showerror("", "Datos no validos")



Button(ventana, text="A hexadecimal", command=convertir).grid(row=1)

ventana.mainloop()
