from datetime import date

print("Programa para calcular Impuesto de Rodamiento")
print("La fecha de hoy es:", date.today())

#datos de entrada
av = float(input("Ingrese el valor del vehiculo: "))
prm = float(input("Dijite e porcentaje de la Renta Municipal: "))
vs = float(input("Valor Semaforizacion: "))
vm = float(input("Dijite el valor de la multa: "))
tim = float(input("tasa de interes mensual: "))

print("Fecha plazo con descuento:")
print("Mes: 1.ENE 2.FEB 3.MAR 4.ARB 5.MAY 6.JUN 7.JUL 8.AGO 9.SEP 10.OCT 11.NOV 12.DIC")
mfpd= int(input("Mes Elejido?"))
dfpd = int(input("Dia?"))

print("Fecha plazo final:")
print("Mes: 1.ENE 2.FEB 3.MAR 4.ARB 5.MAY 6.JUN 7.JUL 8.AGO 9.SEP 10.OCT 11.NOV 12.DIC")
mfpf = int(input("Mes Elejido?"))
dfpd = int(input("Dia?"))

print("Fecha pago:")
print("Mes: 1.ENE 2.FEB 3.MAR 4.ARB 5.MAY 6.JUN 7.JUL 8.AGO 9.SEP 10.OCT 11.NOV 12.DIC")
mfp = int(input("Mes Elejido?"))
dfp = int(input("Dia?"))

#proceso

fpd = date(date.today().year, mfpd , dfpd)
fpf = date(date.today().year, mfpd , dfpd)
fp = date(date.today().year, mfp , dfp)

vi = av * 0.01 * (1 + prm /100) + vs

if fp <= fpd:
    vi = vi * 0.9
else:
    if fp > fpf:
        
        dm = (fp - fpf).days / 30
        vi = vi * (1 + dm * tim/100) + vm

print("El valor del impuesto es:", vi)






