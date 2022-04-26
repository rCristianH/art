#cargar la "GUI libreria" 
from tkinter import *

#crear la ventana
ventana = Tk()
#nombre de la ventana
ventana.title("Calculo de semana Santa")
#tamaño de la ventana
ventana.minsize(200, 50)

#agregar etiqueta
Label(ventana, text="Año a calcular:").grid(row=0, column=0)

#caja de entrada de texto !no obligatorio txt!!
txtAño = Entry(ventana, width=11)
txtAño.grid(row=0, column=1)

txtFecha = Entry(ventana, width=11)
txtFecha.grid(row=1, column=1)
txtFecha.configure(state=DISABLED)

#algoritmo se incluye antes de ser llamado
def obtenerSemanaSanta():
    
    #datos de entrada
    año = int(txtAño.get())

    #proceso
    a = año % 19
    b = año % 4
    c = año % 7
    d = (19 * a + 24) % 30
    dias = d + (2*b + 4*c + 6*d + 5)% 7

    dia = 15 + dias
    mes = "Marzo"

    #codicional
    if dia > 31:
        mes = "abril"
        dia = dia - 31

    txtFecha.configure(state=NORMAL)
    txtFecha.delete(0, END)
    txtFecha.insert(0, str(dia) + " de " + mes)
    txtFecha.configure(state=DISABLED)


#BOTON
Button(ventana, text="Calcular", command=obtenerSemanaSanta).grid(row=1, column=0)





