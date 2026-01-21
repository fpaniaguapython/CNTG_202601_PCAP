class Persona:
    familia_animal = "Mamífero" # Atributo de clase

    def __init__(self, nombre, fecha_nacimiento):
        self.nombre = nombre # Atributo de instancia
        self.fecha_nacimiento = fecha_nacimiento # Atributo de instancia

    def saludar(self):
        print(f'Hola, soy {self.nombre}')

persona1 = Persona('Carlos','01/05/1978')
persona2 = Persona('Anna','08/03/1970')
persona3 = Persona('Carmen','01/01/1970')
print(persona1.familia_animal) # Mamífero --> NO UTILIZAR
print(persona2.familia_animal) # Mamífero --> NO UTILIZAR
print(Persona.familia_animal) # Mamífero
persona3.ciudad = 'Vigo' # Crear un atributo de instancia para persona3
Persona.familia_animal = 'Humanoide' # Modificando el atributo de clase
persona3.familia_animal = 'Bípedo' # ATENCIÓN - ERROR - Creando un atributo de instancia
print('Final de la ejecución')

print(persona2.__dict__) # {'nombre': 'Anna', 'fecha_nacimiento': '08/03/1970'}
print(Persona.__dict__) # {'familia_animal': 'Humanoide', '__init__':  <function Persona.__init__ at 0x0000018E719C7270>, 'saludar': <function Persona.saludar at 0x0000018E719C7320> }
