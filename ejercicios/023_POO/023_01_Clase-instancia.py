class Factura:
    def __init__(self, numero_factura, nombre_cliente, fecha):
        self.numero_factura = numero_factura
        self.nombre_cliente = nombre_cliente
        self.fecha = fecha
        self.pagada = False

entero = int("10")
decimal = float(20)
factura_1 = Factura(1, 'Alex', '2026/01/19')
factura_2 = Factura(3, 'Carmen', '2026/01/18')

