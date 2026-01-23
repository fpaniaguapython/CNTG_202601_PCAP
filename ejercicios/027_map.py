lista = [1, 2, 3]
# Función map 'normal'
def calcular_doble(numero):
    return numero*2
dobles = map(calcular_doble, lista)
print('Sin lambda:')
for doble in dobles:
    print(doble)

# Función map 'con lambda'
dobles = map(lambda numero : numero * 2, lista)
print('Con lambda:')
for doble in dobles:
    print(doble)

# Función map 'normal'
lista = ['imagen.png','fichero.jpeg','selfie.png']
# Utilizando map, mostrar todos los nombres de fichero sin la extensión
def get_nombre_sin_extension(nombre_fichero : str):
    posicion_punto = nombre_fichero.index('.')
    nombre_sin_extension = nombre_fichero[0:posicion_punto]
    return nombre_sin_extension
    # return nombre_fichero[0:nombre_fichero.index('.')]

resultado = map(get_nombre_sin_extension, lista)
for item in resultado:
    print(item)

# Mismo ejercio con lambda
resultado = map(lambda nombre_fichero : nombre_fichero[0:nombre_fichero.index('.')], lista)
for item in resultado:
    print(item)