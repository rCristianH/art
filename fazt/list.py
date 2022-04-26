n = 10

lista_pueba = [1, 2, 3, 4, 5, [1, 2, 3]]
colors = ["r", "g", "b"]

#crear lsita
new_list = list((1, 2, 3, 5, 6, 7, 9))
print(new_list)
#imprimir el tipo de lista
print(type(new_list))

#crear una lista en un rango
nl = list(range(1, n + 1))
print(nl)

#longitud de la lista colors
print(len(colors))

#imprimir la posicion 2 de colors
print(colors[2])
print(colors[-2])

#preguntar si dato r esta en colors
print("r" in colors)

#imprimir lista colors
print(colors)
colors[1] = "y"
print(colors)

#agregar un elemennto de lista
colors.append("v")
print(colors)
colors.append(("e", "b"))
print(colors)
#para agregar varios elementos a lista 
colors.extend(["p", "o"])
print(colors)

#insertar elemnto en lugar especifico
colors.insert(4, "w")
print(colors)

#eliminar objetos de lista
colors.pop(5)
print(colors)

#remover varios objetos
colors.remove("y")
print(colors)

#limpiar lista
colors.clear()
print(colors)

####
colors.extend(["g", "e", "v", "n", "r", "t"])
print(len(colors))

#ordenar alfabeticamentw
colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)

#consultar donde esta r
print(colors.index("r"))

###
colors.append("r")
colors.append("r")

#contar cuantas veces esta r
print(colors.count("r"))
