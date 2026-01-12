nombre_usuario = input('Nombre:')
edad_usuario = int(input('Edad:'))
if edad_usuario>=18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad. No puedes pasar.')
print('Tu nombre es',nombre_usuario,'y tu edad es',edad_usuario)
print(f'Tu nombre es {nombre_usuario} y tu edad es {edad_usuario}')