from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import re

v = Tk()
v.wm_title("Conversion U.C. S.A.")
v.minsize(400,200)

Label(v, text="Unidad Origen").grid(row=0, column=0)
Label(v, text="Cantidad").grid(row=1, column=0)
Label(v, text="Unidad Destino").grid(row=2, column=0)

cmbUnidadOrigen = Combobox(v)
cmbUnidadOrigen.grid(row=0, column=1)
cmbUnidadOrigen["values"] = ["Barril", \
                            "Galón", \
                            "Cuarto", \
                            "Pinta", \
                            "Onza"]

txtCantidad = Entry(v, width=10)
txtCantidad.grid(row=1, column=1)

cmbUnidadDestino = Combobox(v)
cmbUnidadDestino.grid(row=2, column=1)
cmbUnidadDestino["values"] = ["Barril", \
                            "Galón", \
                            "Cuarto", \
                            "Pinta", \
                            "Onza"]
txtCantidadDestino = Entry(v, width=10)
txtCantidadDestino.grid(row=3, column=1)
txtCantidadDestino.configure(state=DISABLED)

def Convertir():
    if cmbUnidadOrigen.current()>=0 and cmbUnidadDestino.current()>=0 and \
       re.match("^[0-9]+[.]?[0-9]*$", txtCantidad.get()):
        uo = cmbUnidadOrigen.current()
        ud = cmbUnidadDestino.current()
        co = float(txtCantidad.get())

        #proceso
        if uo == 0:
            #Barril
            cd = co * 2688
        elif uo == 1:
            #Galón
            cd = co * 64
        elif uo == 2:
            #Cuarto
            cd = co * 16
        elif uo == 3:
            #Pinta
            cd = co * 8
        else:
            #Onza
            cd = co

        if ud == 0:
            #Barril
            cd = cd / 2688
        elif ud == 1:
            #Galón
            cd = cd / 64
        elif ud == 2:
            #Cuarto
            cd = cd / 16
        elif ud == 3:
            #Pinta
            cd = cd / 8


        txtCantidadDestino.configure(state=NORMAL)
        txtCantidadDestino.delete(0, END)
        txtCantidadDestino.insert(0, cd)
        txtCantidadDestino.configure(state=DISABLED)
    else:
        messagebox.showerror("", "Datos no son válidos")

Button(v, text="Convertir", command=Convertir).grid(row=3, column=0)
