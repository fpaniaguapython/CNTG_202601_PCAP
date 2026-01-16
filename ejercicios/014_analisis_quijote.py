# Opción 1
# fichero = open('quijote.txt',mode='rt',encoding='utf-8')
# texto = fichero.read()
# fichero.close()

# Opción 2
with open('quijote.txt',mode='rt',encoding='utf-8') as fichero:
    texto = fichero.read()

palabra = input('Introduce la palabra:')
if (palabra.upper() in texto.upper()):
    print('Existe')
else:
    print('No existe')