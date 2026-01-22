lista = [1, 2, 3, 4, 5]
# Objetivo: obtener una lista con los números de lista * 2
# Método convencional
lista_dobles = []
for numero in lista:
    lista_dobles.append(numero*2)
print(lista_dobles)
# List comprenhension
lista_triples = [numero*3 for numero in lista]
print(lista_triples)
# Crear un lista con los nombres de la lista original convertidos a mayúsculas
nombres = ('Raxo', 'Tortilla', 'pulpo', 'calamares')

nombres_mayusculas = [nombre.upper() for nombre in nombres] # Ojo a los corchetes
print(type(nombres_mayusculas)) # <class 'list'>
print(nombres_mayusculas)

# Creación de un generador a partir de una tupla (o lista o similar)
nombres_mayusculas = (nombre.upper() for nombre in nombres) # Ojo a los paréntesis
print(type(nombres_mayusculas)) # <class 'generator'>
for nombre_mayuscula in nombres_mayusculas:
    print(nombre_mayuscula)