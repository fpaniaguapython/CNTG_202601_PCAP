import random
NUMERO_MINIMO = 0
NUMERO_MAXIMO = 9
NUMERO_INTENTOS = 3
numero_secreto = random.randint(NUMERO_MINIMO,NUMERO_MAXIMO)
for intento in range(NUMERO_INTENTOS):
    numero_candidato = int(input('Introduce el número candidato:'))
    if (numero_candidato==numero_secreto):
        print('¡Adivinado!')
        break # Termina el bucle
    else:
        print('Error')
else:
    print(f'Eres un fraude de adivino. El número secreto era {numero_secreto}')