# Lectura - Opción 1 - open-close
fichero = open('032_lectura_ficheros.py', mode='rt', encoding='utf-8')
#texto = fichero.read() # Lee todo el fichero

# texto = fichero.read(10) # 10 primeros caracteres
# texto = fichero.read(10) # Lee los 10 siguientes caracteres

# texto = fichero.readline() # Lee la primera línea (incluye \n)
# texto.replace('\n','')
# texto = fichero.readline() # Lee la siguiente línea (incluye \n)
# texto.replace('\n','')

# print(texto)

lineas = fichero.readlines()
print(lineas)

fichero.close()
# Lectura - Opción 2 - with-open
with open('032_lectura_ficheros.py', mode='r', encoding='utf-8') as fichero:
    # El close se hace solo
    pass
