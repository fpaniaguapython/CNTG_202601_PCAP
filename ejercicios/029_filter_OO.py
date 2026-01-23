# Crear la clase Automovil - Marca, Modelo, Consumo
# Crear una lista con 5 instancias de Automovil
# Filtrar utilizando lambdas (o no) los automóviles que consumen
# menos de 6 litros.
# Filtrar lo que sean de marca Ferrari.
class Automovil:
    def __init__(self, marca, modelo, consumo):
        self.marca = marca
        self.modelo = modelo
        self.consumo = consumo

    def __str__(self):
        return f'{self.marca}:{self.modelo}:{self.consumo}'

auto1 = Automovil('Ferrari', 'F40', 15)
auto2 = Automovil('Ferrari', 'Testarossa', 4.5)
auto3 = Automovil('Seat', 'Panda', 5)
auto4 = Automovil('Suzuki', 'Alto', 8)
auto5 = Automovil('Ford', 'Fiesta', 4)

autos = [auto1, auto2, auto3, auto4, auto5]
consumo_maximo = 6
autos_consumo_bajo = filter(
    lambda auto_candidato : auto_candidato.consumo<consumo_maximo, autos)

for auto in autos_consumo_bajo:
    print(auto)

autos_ferrari = filter(lambda auto_candidato : auto_candidato.marca=='Ferrari', autos)
for auto in autos_ferrari:
    print(auto)



