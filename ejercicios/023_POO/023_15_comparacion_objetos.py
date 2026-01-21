class Automovil:
    def __init__(self, marca, modelo, consumo):
        self.marca = marca
        self.modelo = modelo
        self.consumo = consumo

    def __eq__(self, other):
        if not isinstance(other, Automovil):
            raise TypeError('Los automóviles solo se pueden comparar con otros automóviles')
        return self.consumo == other.consumo

automovil_1 = Automovil('Seat', '600', 8.1)
automovil_2 = Automovil('Skoda', 'Fabia', 8.1)

print(automovil_1==automovil_2) # == ejecuta el método __eq__
print(automovil_1 is automovil_2) # is - comprueba la identidad
# print(automovil_1=="lagarto") # Error, porque str no tiene consumo

automovil_3 = automovil_2
print(automovil_1 is automovil_2) # False
print(automovil_1 is automovil_3) # False
print(automovil_2 is automovil_3) # True