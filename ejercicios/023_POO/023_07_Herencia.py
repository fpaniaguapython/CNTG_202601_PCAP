class Animal:
    def __init__(self, genoma, nombre, fecha_nacimiento, especie):
        self.genoma = genoma
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.especie = especie
    def alimentarse(self):
        pass
    def reproducirse(self):
        pass

class Buey(Animal):
    def __init__(self, genoma, nombre, fecha_nacimiento, especie, longitud_cuernos):
        super().__init__(genoma, nombre, fecha_nacimiento, especie)
        self.longitud_cuernos = longitud_cuernos
    def tirar(self):
        pass

ramon = Buey("1010111110", "Ramón", "10/06/2021", "Buey", 10)
print(ramon.nombre)
print(ramon.fecha_nacimiento)
print(ramon.longitud_cuernos)
print(isinstance(ramon, Buey)) # True
print(isinstance(ramon, Animal)) # True
    