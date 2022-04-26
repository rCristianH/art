from matplotlib import cm, pyplot as plt
from pandas import pd
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Notebook
from datetime import *
import Util

#Lista de imágenes para los botones
iconos = ['./iconos/grafica.png', \
          './iconos/datos.png'
          ]
textosBotones = ['Gráfica', \
                 'Datos'
                 ]

df = None

def obtenerMonedas():
    global df
    df = pd.read_csv('Cambio Monedas.csv')
    monedas = df['Moneda'].tolist()
    return list(dict.fromkeys(monedas))

def graficar():
    global df, monedas, paneles
    if cmbMoneda.current()>=0:
        df.sort_values(by='Fecha', ascending=False).head()
        cambios =df[df['Moneda']==monedas[cmbMoneda.current()]]
        plt.title('Cambio '+monedas[cmbMoneda.current()])
        plt.ylabel('Cambio')
        plt.xlabel('Fecha')

        #obtener los datos para el eje Y
        y = cambios['Cambio']

        #obtener los datos para el eje X
        fechas = cambios['Fecha']
        #obtener la fecha
        x = [datetime.strptime(f, '%d/%/%Y').date() for f in fechas]

        #Crear la grafica
        plt.clf()
        plt.title('Cambio '+monedas[cmbMoneda.current()])
        plt.ylabel('Cambio')
        plt.xlabel('Fecha')
        #graficar
        plt.plot(x, y)

        #exportar la grafica a una imagen
        plt.savefig('graficaMonedas.png')

        #Mostrar la imagen de la grafica
        lblGrafica=Label(paneles[0])
        imgGrafica=PhotoImage(file = 'graficaMonedas.png')

        lblGrafica.config(image=imgGrafica)
        lblGrafica.image=imgGrafica
        lblGrafica.place(x=0, y=0)
        #redimensionar la ventana de acuerdo a la dimension de la imagen de la grafica
        v.minsize(imgGrafica.width(), imgGrafica.height()+100)


v = Tk()
v.title('Cambios de Moneda')
v.geometry('400x200')
botones = Util.agregarBarra(v, iconos, textosBotones) #Agrega una barra de herramientas

botones[0].configure(command=graficar)

frm = Frame(v)
frm.pack(side=TOP, fill=X)
Util.agregarEtiqueta(frm, 'Moneda:', 0, 0)
monedas=[]
cmbMoneda=Util.agregarLista(frm, monedas, 0, 1)

nb = Notebook(v)
nb.pack(fill=BOTH, expand=YES)
encabezados=['Gráfica', 'Datos']
paneles=[]
for e in encabezados:
    frm = Frame(v)
    paneles.append(frm)
    nb.add(frm, text=e)

lblGrafica=Label(paneles[0])
