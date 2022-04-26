#cargar la libreria para GUI
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
#cargar la libreria para fechas
from datetime import date
#cargar libreria para expresiones regulares
import re

#crear la ventana
ventana = Tk()
ventana.wm_title("Impuesto de Rodamiento")
ventana.minsize(300, 100)

#Agregar las etiquetas
Label(ventana, text="Avalúo del Vehículo").grid(row=0, column=0)
Label(ventana, text="% rentas municipales").grid(row=1, column=0)
Label(ventana, text="Valor semaforización").grid(row=2, column=0)
Label(ventana, text="Valor Multa").grid(row=3, column=0)
Label(ventana, text="Tasa Interés Mensual (%)").grid(row=4, column=0)
Label(ventana, text="Fecha descuento").grid(row=5, column=0)
Label(ventana, text="Fecha final").grid(row=6, column=0)
Label(ventana, text="Fecha pago").grid(row=7, column=0)

#Agregar las cajas de texto
txtAV = Entry(ventana, width=15)
txtAV.grid(row=0, column=1)

txtPRM = Entry(ventana, width=5)
txtPRM.grid(row=1, column=1)

txtVS = Entry(ventana, width=10)
txtVS.grid(row=2, column=1)

txtVM = Entry(ventana, width=10)
txtVM.grid(row=3, column=1)

txtTIM = Entry(ventana, width=5)
txtTIM.grid(row=4, column=1)

txtDFD = Entry(ventana, width=5)
txtDFD.grid(row=5, column=2)

txtDFF = Entry(ventana, width=5)
txtDFF.grid(row=6, column=2)

txtDFP = Entry(ventana, width=5)
txtDFP.grid(row=7, column=2)

txtVI = Entry(ventana, width=15)
txtVI.grid(row=8, column=1, columnspan=2)
txtVI.configure(state=DISABLED)

#Agregar las listas desplegables
cmbMFD = Combobox(ventana)
cmbMFD.grid(row=5, column=1)
cmbMFD["values"] = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

cmbMFF = Combobox(ventana)
cmbMFF.grid(row=6, column=1)
cmbMFF["values"] = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

cmbMFP = Combobox(ventana)
cmbMFP.grid(row=7, column=1)
cmbMFP["values"] = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

#algoritmo
def CalcularImpuesto():
    #validar los datos de entrada
    if re.match("^[0-9]+$", txtAV.get()) and \
    re.match("^[0-9]+[.]?[0-9]*$", txtPRM.get()) and \
    re.match("^[0-9]+$", txtVS.get()) and \
    re.match("^[0-9]+$", txtVM.get()) and \
    re.match("^[0-9]+[.]?[0-9]*$", txtTIM.get()) and \
    re.match("^[0-3]?[0-9]$", txtDFD.get()) and \
    re.match("^[0-3]?[0-9]$", txtDFF.get()) and \
    re.match("^[0-3]?[0-9]$", txtDFP.get()) and \
    cmbMFD.current()>=0 and cmbMFF.current()>=0 and cmbMFP.current()>=0:

        #obtener datos de entrada
        av = int(txtAV.get())
        prm = float(txtPRM.get())
        vs = int(txtVS.get())
        vm = int(txtVM.get())
        tim = float(txtTIM.get())

        fd = date( date.today().year, cmbMFD.current()+1, int(txtDFD.get()))
        ff = date( date.today().year, cmbMFF.current()+1, int(txtDFF.get()))
        fp = date( date.today().year, cmbMFP.current()+1, int(txtDFP.get()))
        
        #proceso
        vi = av * 0.01 * (1 + prm/100) + vs
        if fp <= fd:
            vi = vi * 0.9
        else:
            if fp > ff:
                dm = (fp - ff).days / 30
                vi = vi * (1 + dm * tim/100) + vm

        #mostrar resultados
        txtVI.configure(state=NORMAL)
        txtVI.delete(0, END)
        txtVI.insert(0, vi)
        txtVI.configure(state=DISABLED)
    else:
        messagebox.showerror("", "datos no validos")

#Agregar boton de comando
Button(ventana, text="Calcular", command=CalcularImpuesto).grid(row=8, column=0)







