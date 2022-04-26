from Pila import Pila

frase = input("Frase a validar?")

frase = frase.replace (" ", "").replace("á", "a")

mitad = int(len(frase)/2)
#crear pila para guardar los caracteres hasta la mitad de la frase
p = Pila()
for i in range(0, mitad):
    p.apilar(frase[i])

i = mitad
if len(frase) % 2 == 1:
    i += 1

esPalindromo = True
while not p.vacia() and esPalindromo:
    caracter = p.desapilar() 
    if caracter != frase[i]:
        esPalindromo = False
    i += 1

if esPalindromo:
    print("La frase es palindromo")
else:
    print("La frase No es palindromo")