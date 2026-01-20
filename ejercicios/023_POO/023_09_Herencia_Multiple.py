class Vehiculo:
    def __init__(self, nombre):
        self.nombre = nombre
    def arrancar(self):
        print("Arrancar")
    def parar(self):
        print("Parando vehículo")

class Automovil(Vehiculo):
    def __init__(self, nombre):
        super().__init__(nombre)
    def desplazarse_por_tierra(self):
        print("Desplazándose por tierra")
    def pararx(self):
        print("Parando automóvil")

class Barco(Vehiculo):
    def __init__(self, nombre):
        super().__init__(nombre)
    def desplazarse_por_agua(self):
        print("Desplazándose por agua")
    def pararx(self):
        print("Parando barco")

class Overcraft(Automovil, Barco):
    def __init__(self, nombre):
        super().__init__(nombre)
    def pararx(self):
        print("Parando overcraft")

mi_cacharro = Overcraft("Cacharro")
mi_cacharro.arrancar()
mi_cacharro.desplazarse_por_agua()
mi_cacharro.desplazarse_por_tierra()
mi_cacharro.parar()
