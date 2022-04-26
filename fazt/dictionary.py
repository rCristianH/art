#ejmplo de dicionariio con carro de compras
# al primer '' se le llama keys y al segundo ''items

producto = {
    "name": "book",
    'cantidad': 3,
    'price': 4.99
}

persona = {
    'primer nombre': 'raul',
    'last name': 'alvarez'
}

#pueden haber dicionarios dentro de listas
lista = [
    {
    "name": "book",
    'cantidad': 3,
    'price': 4.99
    },

    {    
    'primer nombre': 'raul',
    'last name': 'alvarez'
    }
]


print(persona)
print(type(persona))

#eliminar un dicionario
del persona
print('Persona ya no exite')


#imprimir las keys de producto
print(producto.keys())


