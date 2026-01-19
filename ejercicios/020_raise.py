def get_saludo(nombre):
    if (nombre.upper()=='ADOLFO'):
        raise ValueError('No quiero saber nada de ti')
    saludo = f'Hola {nombre}'
    return saludo

try:
    nombre = input('Dime tu nombre:')
    saludo = get_saludo(nombre)
    print(saludo)
except ValueError as ve:
    print(ve)