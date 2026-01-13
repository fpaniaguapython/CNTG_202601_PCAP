LIMITE_PESO_BAJO = 18.5
LIMITE_PESO_MEDIO = 25

def calcular_imc(altura : float, peso : int) -> float:
    imc = peso / (altura**2)
    return imc

peso = int(input('Peso:'))
altura = float(input('Altura (metros):'))

imc = calcular_imc(altura, peso)
print('IMC:',imc)
if (imc<LIMITE_PESO_BAJO):
    print('BAJO')
elif (imc<LIMITE_PESO_MEDIO):
    print('OK')
else:
    print('SOBREPESO')
