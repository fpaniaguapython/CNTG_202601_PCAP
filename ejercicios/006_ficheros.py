# 1. Leer el fichero de alergias
fichero = open('alergias.txt',mode='r',encoding='utf-8')
texto = fichero.read()
alergias = texto.split('\n')
fichero.close()

# 2. Leer el fichero de las recetas
fichero = open('receta.txt',mode='r',encoding='utf-8')
texto = fichero.read()
ingredientes = texto.split()
fichero.close()

# 3. Convertir ingredientes a conjunto
ingredientes = set(ingredientes)

# 4. Obtener los ingredientes 'peligrosos'
peligros = ingredientes.intersection(alergias)

# 5. Mostrar los datos:
if len(peligros)>0:
    print('ATENCIÓN')  
    print(peligros)
else:
    print('ADELANTE')

