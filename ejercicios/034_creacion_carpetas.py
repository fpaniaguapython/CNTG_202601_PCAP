import os

propietarios = ['Propietario 1', 'Propietario 2', 'Propietario 3']
ruta_raiz = "c:/borrar/"
for propietario in propietarios:
    os.mkdir(ruta_raiz+propietario)