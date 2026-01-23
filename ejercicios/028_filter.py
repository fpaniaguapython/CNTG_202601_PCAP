lista = [1, 2, 3, 4]

# Sin lambda
def es_par(numero):
    return numero%2==0

resultado = filter(es_par, lista)
for item in resultado:
    print(item)

# Con lambda
resultado = filter(lambda numero : numero%2==0, lista)
for item in resultado:
    print(item)