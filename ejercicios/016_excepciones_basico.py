# resultado = 1/0 # ZeroDivisionError
# lista = [1, 2, 3]
# print(lista[5])  # IndexError
diccionario = {"Joaquin" : 100_000_000, "Iago" : 250_000}
# print(diccionario["Iago"])
# print(diccionario["Carmen"]) # KeyError

# Ejemplo 1 - Except sin especificar
nombre = input('Introduce un nombre:')
try:
    saldo = diccionario[nombre]
    print(f'Saldo de {nombre} es {saldo}')
except:
    print('Tipo 1: Error')

# Ejemplo 2 - Except con tipo
nombre = input('Introduce un nombre:')
try:
    saldo = diccionario[nombre]
    print(f'Saldo de {nombre} es {saldo}')
except KeyError as ke:
    print('Tipo 2:', ke)

# Ejemplo 3 - Except múltiple
diccionario = {"Joaquin" : 100_000_000, "Iago" : "Deudas"}
nombre = input('Introduce un nombre:')
try:
    saldo = diccionario[nombre]
    saldo = int(saldo)
    print(f'Saldo de {nombre} es {saldo}')
except KeyError as ke:
    print('Tipo 3:', ke)
except ValueError as ve:
    print('Tipo 4:', ve)
except BaseException as be:
    print('Tipo 5', be)