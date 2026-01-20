class Cartera:
    def __init__(self, propietario, saldo):
        self.propietario = propietario
        self.__saldo = saldo

    def __validar_saldo(self):
        pass

    def agregar_fondo(self, fondo):
        self.__saldo = self._saldo + fondo
        
    def __str__(self):
        return f'La cartera de {self.propietario} tiene {self.__saldo}€'

cartera_miguel = Cartera('Miguel', 10_000)
print(cartera_miguel.propietario)
# print(cartera_miguel.__saldo) # Error
print(cartera_miguel._Cartera__saldo) # 10000
