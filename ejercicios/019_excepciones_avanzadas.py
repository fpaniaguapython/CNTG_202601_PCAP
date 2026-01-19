try:
    numero_1 = int(input('Número 1:'))
    numero_2 = int(input('Número 2:'))
except ValueError as ve:
    print('Los números deben ser enteros')
else: # Opcional que exista, pero se ejecuta si el try no da error
    resultado = numero_1 + numero_2
    print(resultado)
finally: # Opcional que exista, pero siempre se ejecuta
    print('Siempre se ejecuta')
