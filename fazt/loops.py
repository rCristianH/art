foods = ['apple', 'bread', 'limon', 'toronja']

#imprimir la lista
for i in foods:
    print(i)
print("\n")


#break
for i in foods:
    if i == "limon":
        break
    print(i)

#mostar los numeros de 1, 90 cada dos numeros
for i in range (1, 90, 2):
    print(i)

#imprimir los caracteres de un str
for i in "27":
    print(i)


#imprimir numeros siempre que se cumpla tal condicion
count = 4
while count <= 10:
    print(count)
    count += 1

