
# si no entra nada en la variable name tomara como dato human
def hello(name = 'human'):
    print('Hello ' + name)

a = input("Cual es tu nombre ")
hello(a) 

#suma unos numeros
def add(n1, n2):
    return n1+n2

print(add(10, 90))