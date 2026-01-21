class Metralleta:
    def disparar(self):
        print('Disparando metralleta...')

class Cañón:
    def disparar(self):
        print('Disparando cañón...')

class Vehiculo:
    def __init__(self, nombre):
        self.nombre = nombre
    def avanzar(self):
        print('Avanzando...')
    def parar(self):
        print('Parando...')
    def agregar_arma(self, arma):
        self.arma = arma
    def disparar(self):
        self.arma.disparar()

auto = Vehiculo('V1')
metralleta = Metralleta()
cañón = Cañón()
# auto.agregar_arma(metralleta)
auto.agregar_arma(cañón)
auto.disparar()

