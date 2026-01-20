# Crear las clases Vehiculo, VehiculoTerrestre, Barco, Automovil y Motocicleta

class Vehiculo:
    def __init__(self, marca, modelo, identificador):
        self.marca = marca
        self.modelo = modelo
        self.identificador = identificador
    def deplazar(self):
        print('Soy un vehículo y me estoy desplazando')

class VehiculoTerrestre(Vehiculo):
    def __init__(self, marca, modelo, identificador, numero_ruedas):
        super().__init__(marca, modelo, identificador)
        self.numero_ruedas = numero_ruedas
    def rozar(self):
        print("Soy un vehículo terrestre y estoy rozando el suelo")

class Barco(Vehiculo):
    def __init__(self, marca, modelo, identificador, calado):
        super().__init__(marca, modelo, identificador)
        self.calado = calado
    def atracar(self):
        print("Soy un barco y estoy atracando")

class Automovil(VehiculoTerrestre):
    def __init__(self, marca, modelo, identificador, numero_ruedas, numero_puertas):
        super().__init__(marca, modelo, identificador, numero_ruedas)
        self.numero_puertas = numero_puertas
    def transportar_grupos(self):
        print("Soy un automovil y estoy transportando un grupo")

class Motocicleta(VehiculoTerrestre):
    def __init__(self, marca, modelo, identificador, numero_ruedas, numero_alforjas):
        super().__init__(marca, modelo, identificador, numero_ruedas)
        self.numero_alforjas = numero_alforjas
    def tumbarse(self):
        print("Soy una motocicleta y me estoy tumbando")
    def desplazar(self):
        print("Soy una motocicleta y me estoy desplazando")

auto1 = Automovil("Seat", "600", "CC-8381-A", 4, 5)
auto1.transportar_grupos()
auto1.rozar()
auto1.deplazar()

moto1 = Motocicleta("BMW", "TURBO", "CO-8314-B", 2, 2)
moto1.desplazar()