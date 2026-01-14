import hashlib
# Solicitar password de registro
password = input('Introduce una password:')
# Generar resumen
generador_resumen = hashlib.sha256() 
bytes = password.encode('utf-8')
generador_resumen.update(bytes)
resumen = generador_resumen.digest()
# Almacenar resumen
fichero = open('password.txt',mode='wb')
fichero.write(resumen)
fichero.close()
# Solicitar password de verificación
password_acceso = input('Introduce password:')
# Obtener resumen
generador_resumen_2 = hashlib.sha256() 
bytes = password_acceso.encode('utf-8')
generador_resumen_2.update(bytes)
resumen_2 = generador_resumen_2.digest()
# Leer el resumen almacenado
fichero = open('password.txt','rb')
resumen_almacenado = fichero.read()
fichero.close()
# Verificamos la contraseña
if resumen_2==resumen_almacenado:
    print('OK')
else:
    print('KO')
