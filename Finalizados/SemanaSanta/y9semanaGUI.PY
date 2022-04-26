#Cargar libreria para GUI (Interfaz Grafica)
from tkinter import *

#Crear la ventana
ventana=Tk()
ventana.title("Cálculo semana santa")
ventana.minsize(300,200)

#Agregar etiqueta
Label(ventana,text="Año a calcular:").grid(row=0, column=0)

#Agregar cajas de texto
txtAño=Entry(ventana, width=10)
txtAño.grid(row=0,column=1)
txtFecha=Entry(ventana, width=10)
txtFecha.grid(row=1,column=1)
txtFecha.configure(state=DISABLED)

def obtenerSemanaSanta():
    
    #Datos entrada
    año=int(txtAño.get())
    #Procesos
    a=año%19
    b=año%4
    c=año%7
    d=(19*a+24)%30
    dias=d+(2*b+4*c+6*d+5)%7
    dia=15+dias
    mes="Marzo"
    if dia>31:
        mes="Abril"
        dia=dia-31
    #Datos salida
    txtFecha.configure(state=NORMAL)
    txtFecha.insert(0,str(dia)+" de "+mes)
    txtFecha.configure(state=DISABLED)
    
#Agregar boton
Button(ventana,text="Calcular", command=obtenerSemanaSanta).grid(row=1,column=0)
