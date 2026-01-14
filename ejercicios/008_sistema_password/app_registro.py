import getpass
import digest_manager
import files_manager

if __name__=='__main__':
    email = input('Introduce email:')
    password = getpass.getpass('Introduce password:')
    resumen = digest_manager.generar_resumen(password)
    files_manager.guardar_bytes(nombre_fichero='resumen_password.txt', bytes=resumen)