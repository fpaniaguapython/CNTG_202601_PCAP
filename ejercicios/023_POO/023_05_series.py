# La clase Participante tiene:
# nombre, nacionalidad, nombre del papel
class Participante:
    def __init__(self, nombre, nacionalidad, nombre_papel):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.nombre_papel = nombre_papel
    def __str__(self):
        return f'{self.nombre}:{self.nacionalidad}:{self.nombre_papel}'
    def __repr__(self):
        return f'{self.nombre}:{self.nacionalidad}:{self.nombre_papel}'

# La clase Serie tiene:
# título, género, número de temporadas, plataforma, participantes
class Serie:
    def __init__(self, titulo, genero, numero_temporadas, plataforma, 
                 participantes : list):
        self.titulo = titulo
        self.genero = genero
        self.numero_temporadas = numero_temporadas
        self.plataforma = plataforma
        self.participantes = participantes

    def __str__(self):
        return f'{self.titulo}:{self.genero}:{self.numero_temporadas}:{self.plataforma}:{self.participantes}'

    def __repr__(self):
        return f'{self.titulo}:{self.genero}:{self.numero_temporadas}:{self.plataforma}:{self.participantes}'

# Modelar las clases
# Crear un objeto serie que tenga al menos 3 participantes
# Mostrar toda la información de una serie (todos los atributos de Serie) y
# todos lode Participante

pennywise = Participante("Bill Skarsgård", "Sueco", "Pennywise")
charlotte = Participante("Taylour Paige", "Norteamericana", "Charlotte Hanlon")
marge = Participante("Matilda Lawler", "Norteamericana", "Marge")
lista_participantes = [pennywise, charlotte, marge]

bienvenidos_a_derry = Serie("It: Bienvenidos a Derry", "Terror", 1, "HBO", lista_participantes)

print(bienvenidos_a_derry)

