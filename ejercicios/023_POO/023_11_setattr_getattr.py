class Pedido:
    def __init__(self, cliente, producto, cantidad):
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad

pedido1 = Pedido('Jacobo', 'Leche', 100)
# Acceso de lectura a atributos
print(pedido1.producto)
print(getattr(pedido1,'cantidad'))
print(getattr(pedido1, 'cantidad', 0)) # Por defecto, devuelve un 0 si no hay atributo importe

# Acceso de escritura de un atributo
pedido1.producto='Vino' # Asigna un valor 
setattr(pedido1, 'nombre', 'Israel') # Asigna un valor
pedido1.fecha_entrega = '22/01/2026' # Crea un atributo y le asigna un valor
setattr(pedido1, 'fecha_pedido', '22/01/2026') # Crea un atributo y le asigna un valor
