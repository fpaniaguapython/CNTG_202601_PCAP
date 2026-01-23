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

# El atributo key recibe la función que 'cuantifica' el objeto para poder
# compararlo y ordenarlo
autos_ordenados = sorted(autos, key=lambda auto : auto.consumo, reverse=True)
for auto in autos_ordenados:
    print(auto)