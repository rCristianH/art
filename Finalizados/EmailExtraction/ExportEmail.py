import re

str = "Please contact info@sololearn.com.co ccrhdbj@outlook.com for assistance"

pattern = r"[\w\.-]+@[\w\.-]+\.[\w\.]+"

#DOC
"""
([\w\.-]+): Coincide con uno o mas caracteres alfanumericos punto o barra 
            Contiene una cadena con plabras y barra y punto permitido
@: Seguido de un @
([\w\.-]+): Coincide con uno o mas caracteres alfanumericos punto o barra 
(\.[\w\.]+): Un punto y otra palabra

1. La primera parte de la direcion de correo
2. El nombre de dominio sin el subfijo
3. Subfijo del dominio
"""

#Varias direciones
match = re.findall(pattern, str)
if match:
    for i in match:
        print(i)
#One direcion
""" match = re.search(pattern, str)
if match:
    print(match.group())
 """
