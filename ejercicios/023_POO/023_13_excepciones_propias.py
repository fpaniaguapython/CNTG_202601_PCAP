class ArchienemigoError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

    def write_log(self):
        print('Ha ocurrido un error el día 21/01 a las 18:19')

def saludar(nombre : str):
    if not isinstance(nombre, str):
        raise TypeError('El nombre debe ser un str')
    if nombre=='Pedro':
        raise ArchienemigoError('Pedro no es válido', True, 10.3, ['Uno','Dos'])
    print(f'Hola {nombre}')

try:
    saludar('Pedro')
except TypeError as te:
    print(te)
except ArchienemigoError as ae:
    ae.write_log()
    print(ae)
    print(ArithmeticError.__subclasses__()) # [<class 'FloatingPointError'>, <class 'OverflowError'>, <class 'ZeroDivisionError'>]        
    print("Atributo args:", ae.args) # Muestra todos los argumentos