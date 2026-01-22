class Persona:
    def __init__(self, cabeza, cuerpo, brazo_der, brazo_izq, pierna_der, pierna_izq):
        self.cabeza = cabeza
        self.cuerpo = cuerpo
        self.brazo_der = brazo_der
        self.brazo_izq = brazo_izq
        self.pierna_der = pierna_der
        self.pierna_izq = pierna_izq
        self.__partes = (self.cabeza, self.cuerpo, self.brazo_der, self.brazo_izq, self.pierna_der, self.brazo_izq)
        self.__contador = 0

    def __iter__(self): # Devuelve al objeto como iterador
        return self
    
    def __next__(self): # Devuelve al siguiente elemento del iterable
        if self.__contador==len(self.__partes):
            self.__contador=0 # Inicializamos el contador a 0 para la siguiente iteración
            raise StopIteration() # Le dice al bucle '¡ya he terminado!'
        parte = self.__partes[self.__contador]
        self.__contador+=1
        return parte

israel = Persona('Cabeza','Cuerpo','Brazo derecho', 'Brazo izquierdo', 'Pierna derecha', 'Pierna izquierda')

for parte in israel:
    print(parte)

for parte in israel:
    print(parte)