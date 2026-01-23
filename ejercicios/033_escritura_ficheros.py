nombre = input('Introduce tu nombre:')
with open('mi_nombre.txt', mode='wt', encoding='utf-8') as fichero:
    fichero.write(nombre)
    fichero.write('\n') # Escribe un salto de línea

