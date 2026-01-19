nombre_fichero = input('Introduce un nombre de fichero:')

try:
    fichero = open(nombre_fichero, mode='r', encoding='utf-8')
    datos = fichero.read()
    print(datos)
    fichero.close()
except FileNotFoundError as fne:
    print(f'El fichero {nombre_fichero} no existe')