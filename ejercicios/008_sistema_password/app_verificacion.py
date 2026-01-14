import getpass
import digest_manager
import files_manager

if __name__=='__main__':
    email = input('Introduce email:')
    password = getpass.getpass('Introduce password:')
    resumen = digest_manager.generar_resumen(password)
    resumen_almacenado = files_manager.leer_bytes('resumen_password.txt')
    if (resumen==resumen_almacenado):
        print('OK')
    else:
        print('KO')