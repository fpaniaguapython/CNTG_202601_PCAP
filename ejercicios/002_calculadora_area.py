'''
Crea un programa en Python
que pida ancho y alto de un rectángulo
y calcule el área
'''
def calcular_area(ancho, alto):
    area = ancho * alto
    return area

ancho = float(input('Introduce ancho:'))
alto = float(input('Introduce alto:'))
resultado = calcular_area(ancho, alto)
print(resultado)