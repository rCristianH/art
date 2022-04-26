print ("Programa para calcular el valor de una deuda")

#Escribe todas las variables comenzando con mayuscula!!

#Datos de entrada
Monto = float(input("Monto a prestar?"))
Tasa = float(input("Tasa de interes?"))
Plazo = float(input("Numero de cuotas"))

#Proceso
Tasa = Tasa / 100
x = (1 + Tasa)**Plazo
Cuota = Monto * x * Tasa /(x - 1)

#Mostrar resultados
print("El valor de la cuota es ", Cuota)
