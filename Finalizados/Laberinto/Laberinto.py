from classCola import Cola

class Punto():

    def __init__(varClase, x, y):
        varClase.x = x
        varClase.y = y

    def esIgual(varClase, punto):
        return varClase.x == punto.x and varClase.y == punto.y


class Laberinto():

    def __init__(varClase, laberinto, \
                 xEntrada, yEntrada, \
                 xSalida, ySalida):
        varClase.entrada = Punto(xEntrada, yEntrada)
        varClase.salida = Punto(xSalida, ySalida)
        varClase.laberinto = laberinto

        varClase.filas = len(laberinto)
        varClase.columnas = len(laberinto[0])

    def mostrar(varClase):
        for i in range(0, varClase.filas):
            linea=""
            for j in range(0, varClase.columnas):
                if varClase.laberinto[i][j] == 1:
                    linea += "|"
                elif varClase.laberinto[i][j] == 0:
                    linea += "*"
                else:
                    linea += str(varClase.laberinto[i][j])
            print(linea)

    def asignar(varClase, punto, valor):
        varClase.laberinto[Punto.x][Punto.y] = valor

    def estaLibre(varClase, unPunto):
        return varClase.laberinto[unPunto.x][unPunto.y] == 0

    def resolver(varClase):
        cola = Cola()
        varClase.asignar(varClase.salida, 0) # marcar el puntode salida
        varClase.mostrar()

        punto = varClase.inicio
        cola.encolar(punto)
        varClase.asignar(punto, -1) # Asignarlo a -1 para evitar retroceder y repetir la búsqueda
        while not cola.vacia(): 
            punto = cola.desencolar()
            if punto.esIgual(varClase.salida): # Salida encontrada, ruta de salida
                return True # Devuelve true cuando se encuentra una ruta
            for di in range(0, 4): # escanea cíclicamente cada posición
                heAvanzado = False
                if di == 0 and punto.x>0:
                    #avanzar A LA IZQUIERDA 
                    heAvanzado = True
                    puntoInteres=Punto(punto.x-1, punto.y)
                elif di == 1 and punto.y<varClase.columnas-1:
                    #avanzar hacia ABAJO
                    heAvanzado = True
                    puntoInteres=Punto(punto.x, punto.y+1)
                elif di == 2 and punto.x<varClase.filas-1:
                    #avanzar a la derecha
                    heAvanzado = True
                    puntoInteres=Punto(punto.x+1, punto.y)
                elif di == 3 and punto.y>0:
                    #avanzar hacia arriba 
                    heAvanzado = True
                    puntoInteres=Punto(punto.x, punto.y-1)

                if heAvanzado:
                    if varClase.estaLibre(puntoInteres):
                        cola.encolar(puntoInteres)
                        varClase.asignar(puntoInteres, -1)

        return False


