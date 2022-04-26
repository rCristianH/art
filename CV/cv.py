print("Programa para calcular los CV")
m = float(input("ingrese la distancia en metros: "))
seg = float(input("Ingrese el tiempo en segundos: "))
kg = float(input("Ingrese el peso en KG: "))
g = 9.8
cvf = 735

#ejecucion
newtons = kg * g
julius = newtons * m
potencia = julius / seg
cv = potencia / cvf



print("La cantidad de cv utilizados para hacer " + str(m) + " metros, fue de " + str(cv) + "CV")

