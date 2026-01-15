import random

x = random.random() # [0,1)
print(x) # Cada ejecución produce un nuevo número
random.seed(18) # Indicación de la semilla (un número, una cadena...). 
x = random.random() # Siempre genera el mismo número
print(x)
x = random.random() # Siempre genera el mismo número
print(x)

random.seed() # Inicializa la semilla con el reloj del sistema
x = random.randrange(0,10) # Entre 0 (incluido) y 10 (no incluido)
print(x)

x = random.randint(0,10) # Entre 0 (includo) y 10 (incluido)
