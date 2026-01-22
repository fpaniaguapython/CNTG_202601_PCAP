import time
# Versión 'convencional'
def get_pares_normal(limite):
    pares = []
    for numero in range(0,limite, 2):
        time.sleep(1) # Espera un segundo
        pares.append(numero)
    return pares

print('Inicio del cálculo "normal"')
pares = get_pares_normal(10)
print(pares)
print('Fin del cálculo "normal"')

# Versión con generador
def get_pares_generador(limite):
    for numero in range(0,limite, 2):
        time.sleep(1) # Espera un segundo
        yield numero

print('Inicio del cálculo "generador"')
generador = get_pares_generador(10)
for par in generador:
    print(par)
print('Fin del cálculo "generador"')

#Si se hace otro for sobre el generador no muestra nada, porque está 
#agotado (se ha recorrido por completo). Se debe crear un nuevo generador.
