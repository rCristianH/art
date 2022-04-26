from tkinter import *
from tkinter import messagebox
#importar libreria de pestaña
from tkinter.ttk import Notebook
from Jugador import Jugador

v = Tk()
v. title("Juego del apuntado")
v.minsize(width=630, height=270)

#crear menu prin
mnuP = Menu(v)
#agregar a la aventana
v.config(menu=mnuP)

j1 = Jugador()
j2 = Jugador()

def repartir():
    global j1, j2
    j1.repartir()
    j2.repartir()
    j1.mostrar(f1)
    j2.mostrar(f2)
    
def verificar():
    global j1, j2
    if nbJ.index(nbJ.select()) == 0:
        messagebox.showinfo("Martin Contreras", j1.verificar())
    else:
        messagebox.showinfo("Raul Vidal", j2.verificar())

def salir():
    v.destroy()
    quit()

#opciones del menu
mnuJ = Menu(mnuP)
#add comando para agregar opciones 
mnuJ.add_command(label="Repartir", command=repartir)
mnuJ.add_command(label="Verificar", command=verificar)


mnuP.add_cascade(label="Juego", menu=mnuJ)
mnuJ.add_command(label="Salir", command=salir)

#Definir pestañas del Juego
nbJ = Notebook(v)
nbJ.pack(fill="both", expand="yes")

f1 = Frame(nbJ, bg="green")
f2 = Frame(nbJ, bg="lightblue")

nbJ.add(f1, text="Martin Contreras")
nbJ.add(f2, text="Raul Vidal")
