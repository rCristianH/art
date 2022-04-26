#cargar la libreria para GUI
from tkinter import *
from tkinter import messagebox

v = Tk()
v.title("Raices ecuación cuadrática")

txtA = Entry(v, width=10)
txtA.grid(row=0, column=1)
txtB = Entry(v, width=10)
txtB.grid(row=1, column=1)
txtC = Entry(v, width=10)
txtC.grid(row=2, column=1)

Label(v, text="Coeficiente A:").grid(row=0, column=0)
Label(v, text="Coeficiente B:").grid(row=1, column=0)
Label(v, text="Coeficiente C:").grid(row=2, column=0)

Label(v, text="raíz X1").grid(row=4, column=0)
Label(v, text="raíz X2").grid(row=5, column=0)

txtX1 = Entry(v, width=30)
txtX1.grid(row=4, column=1)
txtX1.configure(state=DISABLED)
txtX2 = Entry(v, width=30)
txtX2.grid(row=5, column=1)
txtX2.configure(state=DISABLED)

def calcularRaices():
    #obtener datos de entrada
    a = float(txtA.get())
    b = float(txtB.get())
    c = float(txtC.get())

    #proceso
    if a != 0:
        r = b**2 - 4 * a * c
    else:
        messagebox.showerror("Error al calcular", "La ecuación no es cuadrática")

Button(v, text="calcular", command=calcularRaices).grid(row=3, column=0, columnspan=2)



