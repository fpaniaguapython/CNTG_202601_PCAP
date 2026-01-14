def guardar_bytes(bytes : bytes , nombre_fichero : str):
    fichero = open(nombre_fichero,mode='wb')
    fichero.write(bytes)
    fichero.close()

def leer_bytes(nombre_fichero : str) -> bytes:
    fichero = open(nombre_fichero,'rb')
    contenido = fichero.read()
    fichero.close()
    return contenido