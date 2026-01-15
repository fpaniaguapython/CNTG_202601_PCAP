import random 

nombres = ('Miguel','María','Fátima','Silvia','Álvaro','Luis')
apellidos = ('Barreiro','Someso','Couto','Fernández','Calviño','Romero')
categorias = ('Ayudante','Programador Junior','Programador Senior','Director')
SALARIO_MINIMO = 10_000
SALARIO_MAXIMO = 120_000
NUMERO_INDIVIDUOS = 1_000

fichero = open('personas.csv',mode='w',encoding='utf-8')
for contador in range(NUMERO_INDIVIDUOS):
    nombre = random.choice(nombres)
    primer_apellido = random.choice(apellidos)
    segundo_apellido = random.choice(apellidos)
    categoria = random.choice(categorias)
    salario = random.randint(SALARIO_MINIMO, SALARIO_MAXIMO)
    fichero.write(f'{nombre},{primer_apellido},{segundo_apellido},{categoria},{salario}\n')
fichero.close()