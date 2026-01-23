def funcion_externa(numero):
    def funcion_interna():
        print("Ejecutando la función interna:", numero)
        return
    return funcion_interna

numero = 10
f1 = funcion_externa(numero)
numero = 12
f2 = funcion_externa(numero)
input('Pulsa ENTER para ejecutar f1:')
f1() # "Ejecutando la función interna:10
input('Pulsa ENTER para ejecutar f2:')
f2() # "Ejecutando la función interna:12

def calcular():
    pass