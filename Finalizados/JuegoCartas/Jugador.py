from Carta import Carta
from Enumerados import *

class Jugador():

    TOTAL_CARTAS = 10

    def __init__(varClase):
        varClase.cartas = []

    def repartir(varClase):
        varClase.cartas = []
        for i in range(Jugador.TOTAL_CARTAS):
            c = Carta()
            varClase.cartas.append(c)

    def mostrar(varClase, frm):
        x = 10
        for c in varClase.cartas:
            c.mostrar(frm, x, 10)
            x += 40

    def verificar(varClase):
        contadores = []
        for i in range(13):
            contadores.append(0)

        for c in varClase.cartas:
            p = c.obtenerIndiceNumero() - 1
            contadores[p] += 1

        mensaje = "Las figuras encontradas fueron:"  + "\n"
        for i in range(13):
            if contadores[i] >= 2:
                g = GrupoCarta(contadores[i])
                nc = NombreCarta(i+1)

                mensaje += g.name + " de " + nc.name + "\n"
            
        return mensaje


    