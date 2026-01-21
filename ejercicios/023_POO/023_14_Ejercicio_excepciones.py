'''
Programar una clase CuentaBancaria
Atributos:
- IBAN
- Saldo
Métodos:
- IngresarImporte --> Verificar que el importe es entero positivo
- RetirarImporte --> Verificar que hay saldo suficiente. 
  Si no --> NoHaySaldoError
'''
class NoHaySaldoError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class CuentaBancaria:
    def __init__(self, IBAN, saldo):
        self.IBAN = IBAN
        self.saldo = saldo

    def ingresar_importe(self, cantidad):
        if (not isinstance(cantidad, int)):
            raise TypeError('El importe debe ser un número entero')
        if cantidad<=0:
            raise ValueError('El importe debe ser positivo')
        self.saldo=self.saldo+cantidad
        # self.saldo+=cantidad

    def retirar_importe(self, cantidad):
        if cantidad>self.saldo:
            raise NoHaySaldoError('No tienes saldo suficiente')
        self.saldo-=cantidad

    def __str__(self):
        return f'IBAN:{self.IBAN}. Saldo:{self.saldo}'

c1 = CuentaBancaria('ES803843783', 1000)
c1.ingresar_importe(100)
print(c1)
c1.retirar_importe(500)
print(c1)
c1.retirar_importe(600)
print(c1)
c1.retirar_importe(50)
print(c1)