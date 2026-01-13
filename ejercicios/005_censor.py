'''
Crear una lista con palabras prohibidas
Solicitar al usuario que introduzca un 'tweet'
Censurar si ha utilizado ninguna palabra prohibida
'''
palabras_prohibidas = ['arroz','pan','cerveza']
palabras_prohibidas = set(palabras_prohibidas)
texto_tweet = input('Introduce el texto:')
palabras_texto = texto_tweet.split()
if palabras_prohibidas.isdisjoint(palabras_texto):
    print('OK')
else:
    print('BANEADO')
