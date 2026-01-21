class Vehiculo:
    def __init__(self, nombre):
        self.nombre = nombre
    def avanzar(self):
        print('Avanzando...')
    def parar(self):
        print('Parando...')

class VehiculoGuerra(Vehiculo):
    def __init__(self, nombre):
        super().__init__(nombre)
    def disparar(self):
        print("Disparando...")        

vehiculo_guerra = VehiculoGuerra('SKODA')
vehiculo_guerra.avanzar()
vehiculo_guerra.parar()
vehiculo_guerra.disparar()
