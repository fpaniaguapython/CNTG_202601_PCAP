import hashlib

def generar_resumen(texto : str) -> bytes:
    generador_resumen = hashlib.sha256() 
    bytes = texto.encode('utf-8')
    generador_resumen.update(bytes)
    resumen = generador_resumen.digest()
    return resumen