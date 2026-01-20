class CuentaBancaria:
    def __init__(self, nombre_titular, IBAN, saldo_inicial):
        self.nombre_titular = nombre_titular
        self.IBAN = IBAN
        self.saldo = saldo_inicial

    def ingresar(self, cantidad):
        self.saldo+=cantidad

    def retirar(self, cantidad):
        if (cantidad>self.saldo):
            raise ValueError('No tiene saldo suficiente')
        self.saldo-=cantidad

    def transferir(self, cantidad, IBAN, nombre_destinatario, concepto):
        if (cantidad>self.saldo):
            raise ValueError('No tiene saldo suficiente')
        self.saldo-=cantidad
        print(f'Transfiriendo {cantidad} a {nombre_destinatario}')

    def __str__(self) -> str:
        return f'STR:{self.IBAN}:{self.nombre_titular}:{self.saldo}'

    def __repr__(self) -> str:
        return f'REPR:{self.IBAN}:{self.nombre_titular}:{self.saldo}'
    
mi_cuenta = CuentaBancaria('Fernando','ES80X8DF78D7F',10_000)
mi_cuenta.ingresar(50_000)
print(mi_cuenta) # STR:ES80X8DF78D7F:Fernando:60000
lista = [1,'Hola',mi_cuenta]
print(lista) # [1, 'Hola', REPR:ES80X8DF78D7F:Fernando:60000]

