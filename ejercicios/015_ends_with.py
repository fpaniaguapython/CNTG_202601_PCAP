lista = ['nombre.gif', 'cv.docx', 'programa.py', 'datos.jpg', 'selfie.gif', 'enrique.GIF']

# Mostrar los ficheros de la lista con la extensión gif

for nombre_fichero in lista:
    if nombre_fichero.lower().endswith('.gif'):
        print(nombre_fichero)