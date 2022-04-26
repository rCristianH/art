#interfaz grafica de usuario
from tkinter import *

#Importar la libreria para Listas Desplegables
from tkinter.ttk import Combobox

#cajas de de mensajes
from tkinter import messagebox

#Crear la ventana
v = Tk()
v.wm_title("Conversion Hora Militar") 
v.minsize(width=400, height=150)

#Agregar etiquetas
Label(v, text="Hora:").grid(row=0, column=0)
Label(v, text="Jornada:").grid(row=1, column=0)

#Agregar Listas desplegables
cmbHora = Combobox(v, width=5)
cmbHora.grid(row=0, column=1)
cmbHora["values"] =   ["01", "02", \
                    "03", "04", \
                    "05", "06", \
                    "07", "08", \
                    "09", "10", \
                    "11", "12"]

cmbMinuto = Combobox(v, width=5)
cmbMinuto.grid(row=0, column=2)
cmbMinuto["values"] = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", \
                       "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", \
                       "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", \
                       "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", \
                       "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", \
                       "50", "41", "52", "53", "54", "55", "56", "57", "58", "59"]

cmbJornada=Combobox(v, width=5)
cmbJornada.grid(row=1, column=1)
cmbJornada["values"] = ["AM","PM"]

txtHoraMilitar = Entry(v, width=10)
txtHoraMilitar.grid(row=2, column=1)
txtHoraMilitar.configure(state=DISABLED)


def Convertir():
    if cmbHora.current()>=0 and \
    cmbJornada.current()>=0 and \
    cmbMinuto.current()>=0:
        hora = cmbHora.current() + 1
        minuto = cmbMinuto.current()
        jornada = cmbJornada.current()

        horaMilitar = hora
        if jornada == 1:
            if hora < 12:
                horaMilitar = horaMilitar + 12
        else:
            if hora==12:
                horaMilitar = 0

        txtHoraMilitar.configure(state=NORMAL)
        txtHoraMilitar.delete(0, END)
        txtHoraMilitar.insert(0, "{0:02d}{1:02d}".format(horaMilitar, minuto))
        txtHoraMilitar.configure(state=DISABLED)
    else:
        messagebox.showerror("", "datos no validos")
    


Button(v, text="Convertir", command=Convertir).grid(row=2, column=0)




