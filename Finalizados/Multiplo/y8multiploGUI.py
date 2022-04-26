from tkinter import *
from tkinter import messagebox
import re


v = Tk()
v.minsize(300,100)
v.wm_title("Sumatoria de Multiplos")
Label(v, text="Tope de la suma:").grid(row=0, column=0)
Label(v, text="Múltiplos de:").grid(row=1, column=0)

txtN = Entry(v, width=10)
txtN.grid(row=0, column=1)

txtM = Entry(v, width=10)
txtM.grid(row=1, column=1)

txtS= Entry(v, width=10)
txtS.grid(row=2, column=1)
txtS.configure(state=DISABLED)

def CalcularSumatoria():
    #validar datos de entrada
    if re.match("^[0-9]+$", txtN.get()) and re.match("^[0-9]+$", txtM.get()):
        #obtener datos de entrada
        n = int(txtN.get())
        m = int(txtM.get())

        #proceso
        s = 0
        for i in range(m, n+1, m):
            s = s + i

        #mostrar resultados        
        txtS.configure(state=NORMAL)
        txtS.delete(0, END)
        txtS.insert(0, s)
        txtS.configure(state=DISABLED)
            
        
    else:
        messagebox.showerror("", "Dato no valido")

Button(v, text="Calcular", command=CalcularSumatoria).grid(row=2, column=0)
