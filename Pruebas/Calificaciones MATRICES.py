estudiantes = ["ACOSTA DANIEL ", \
	"AGUDELO QUICENO JUANITA ", \
	"ALARCÓN CELIS ALEJANDRO ", \
	"ALDANA MONTEALEGRE JHON JAIRO ", \
	"ALOMIA MANUEL ", \
	"ALZATE POSADA ANA MARÍA ", \
	"ANDREA ROCHA", \
	"AYALA S MARIA CRISTINA", \
	"BARRERA VALDÉS NATALIA ", \
	"BARRERO JOHN", \
	"BEDOYA T JUAN DIEGO ", \
	"BEJARANO PACHÓN JUAN SEBASTIÁN ", \
	"BELTRAN RICO ANDRÉS FELIPE ", \
	"BOHÓRQUEZ CABRERA JUAN JOSÉ ", \
	"BOHÓRQUEZ ESPINOSA ANDREA MILENA ", \
	"BOHORQUEZ IBAÑEZ JIMMY ALEJANDRO ", \
	"BUITRAGO ROBERT ", \
	"CALDERÓN PAULA", \
	"CALLE ESPINOSA CRISTINA ", \
	"CAMPOS CASTELLANOS ANA RAQUEL " ]
	
notas = [[2.4, 3.9, 3.9, 4.2], \
	[3.6, 2.4, 2.9, 4.7], \
	[2.3, 3.3, 2.9, 4.3], \
	[3.7, 3.7, 4.7, 2.9], \
	[4.4, 2.0, 4.6, 3.4], \
	[3.6, 3.3, 2.5, 2.8], \
	[2.6, 4.8, 2.9, 4.3], \
	[4.1, 2.7, 2.1, 2.6], \
	[3.6, 4.0, 4.5, 4.9], \
	[2.4, 2.9, 3.5, 4.8], \
	[2.6, 3.4, 4.2, 3.2], \
	[2.0, 3.3, 4.5, 3.8], \
	[4.5, 2.4, 4.3, 3.0], \
	[3.7, 4.2, 4.6, 4.1], \
	[2.1, 3.6, 2.0, 3.6], \
	[4.4, 2.9, 2.5, 4.3], \
	[3.1, 4.6, 2.6, 4.6], \
	[2.9, 4.9, 4.7, 4.0], \
	[2.5, 4.7, 3.4, 2.6], \
	[3.7, 2.8, 2.2, 4.8]]

porcentajes = [20, 30, 25, 25]

promedios = []

nota=[]
nota.append(3.6)
nota.append(4.0)
nota.append(4.5)
nota.append(4.9)
notas.append(nota)

#notas.append([3.6, 4.0, 4.5, 4.9])
estudiantes.append("PEREZ PEPITO")


#Calcular los promedios de cada estudiante
for fila in range(len(notas)):
    #calcular el promedio del estudiante en la fila
    promedio = 0
    for columna in range(len(notas[0])):
        promedio += notas[fila][columna] * porcentajes[columna]/100
    promedios.append(promedio)
    print(estudiantes[fila], "{0:,.1f}".format(promedio))

#Tomar el primer promedio como el mayor de todos
pm = 0
#Recorrer los restantes promedios
for i in range(1, len(promedios)):
    if promedios[i] > promedios[pm]:
        pm = i

print("El mayor promedio lo obtuvo ", estudiantes[pm], " con un promedio de ",  "{0:,.1f}".format(promedios[pm]))
    




        
    


    
