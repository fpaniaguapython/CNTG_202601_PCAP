# Listas - Delimitadas por corchetes
# Heterogéneo
# Tiene orden
# Mutable
lista = ['Hola',True,10,8.3,[1,2,3]] # Lista
lista.append('otro elemento') # Agrega al final
for elemento in lista: # Recorre la lista
    print(elemento)
lista[2] = 9 # Modificando el tercer elemento de la lista
print(lista[4]) # Mostrando el quinto elemento

# Tuplas - Delimitadas por paréntesis
# Heterogéneo
# Tiene orden
# Inmutable
tupla = ('Primavera','Verano','Otoño','Invierno')
for estacion in tupla:
    print(estacion)
print(tupla[2])

# Conjunto
frutas_invierno = {'Naranja', 'Manzana', 'Limón', 'Naranja'}
frutas_verano = {'Melón', 'Sandía', 'Manzana'}
numero_frutas_invierno = len(frutas_invierno)
numero_frutas_verano = len(frutas_verano)
print(numero_frutas_invierno) # 3
print(numero_frutas_verano) # 3
print(frutas_invierno)
frutas_comunes = frutas_invierno.intersection(frutas_verano)
print(frutas_comunes) # {Manzana}

# Diccionario
diccionario =  {
    "Jacobo":("Jacobo León","Renault Clio"),
    "Israel":("Isreal de los Reyes","Seat 600")
    }

print(diccionario['Israel'])# Acceso al elemento
print(tuple(diccionario.values()))# Conversión de los valores
iago = diccionario.get('Iago',('No encontrado','Sin coche'))
print(iago)
