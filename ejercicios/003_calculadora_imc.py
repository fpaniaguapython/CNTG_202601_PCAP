def calcular_imc(altura : float, peso : int):
    imc = peso / (altura**2)
    return imc

peso = int(input('Peso:'))
altura = float(input('Altura (metros):'))

imc = calcular_imc(altura, peso)
print('IMC:',imc)
if (imc<18.5):
    print('BAJO')
elif (imc<25):
    print('OK')
else:
    print('SOBREPESO')