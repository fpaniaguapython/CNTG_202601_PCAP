numero_1 = input('Introduce número 1:')
numero_2 = input('Introduce número 2:')
try:
    numero_1 = int(numero_1)
    numero_2 = int(numero_2)
    resultado = numero_1 / numero_2
    print('Resultado:',resultado)
except ValueError as ve:
    print('Los números tienen que ser enteros')
except ZeroDivisionError as zde:
    print('No se puede dividir entre cero')
except BaseException as be:
    print('Ha ocurrido un error imprevisto')