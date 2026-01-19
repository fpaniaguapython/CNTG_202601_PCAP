'''
Comprobar que los argumentos son números enteros positivos.
Si no son números enteros -> Generar TypeError
Si no son positivos -> Generar ValueError
'''
def sumar(numero_1 : int, numero_2 : int) -> int:
    if not isinstance(numero_1, int):
        raise TypeError("El primer sumando debe ser un número entero")
    if not isinstance(numero_2, int):
        raise TypeError("El segundo sumando debe ser un número entero")
    if numero_1<0 or numero_2<0:
        raise ValueError("Los sumandos deben ser positivos")
    resultado = numero_1 + numero_2
    return resultado

print(sumar(1,4))