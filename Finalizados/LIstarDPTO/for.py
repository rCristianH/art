from DPColombia import obtenerDeptos
from tkinter import *
import Util
import csv

nombreArchivo = 'ciudades.csv'
campos = ['Dpto', 'Mpio']

tMunicipios = None

def obtenerDpto():
    global nombreArchivo, campos
    dpto= []
    with open(nombreArchivo, newline='',encoding='utf8') as archivoCSV:
        registros = csv.DictReader(archivoCSV, fieldnames=campos, delimiter=';')
        anterior = ''
        for r in registros:
            if r [campos[0]] != anterior:
                anteriorDpto = r[campos[0]]
                dpto.append(anteriorDpto)
    return dpto

def obtenerMunicipios(e):
    global tMunicipios, dpto, campos
    if cmbDpto.current()>=0:
        Dpto = dpto[cmbDpto.current()]
        with open(nombreArchivo, newline='', encoding='utf8') as archivoCSV:
            registros = csv.DictReader(archivoCSV, fieldnames=campos, delimiter=';')
            datos = []

            f = 0
            r = registros.__next__()
            while r[campos[0]] != Dpto:
                r = registros.__next__()
                f += 1
            while r[campos[0]] == Dpto:
                fila = []
                fila.append(r[campos[1]])
                datos.append(fila)
                r = registros.__next__()

            tMunicipios = Util.mostrarTabla(frm, \
                                        ['Municipio'], \
                                        datos, \
                                        tMunicipios)


v = Tk()

Util.agregarEtiqueta(v, 'Departamento:', 0, 0)
dpto=obtenerDeptos()
cmbDpto = Util.agregarLista(v, dpto, 0, 1)

cmbDpto.bind("<<ComboboxSelected>>", obtenerMunicipios)

frm = Frame(v)
frm.grib(row=1, column=0, columnspan=2)