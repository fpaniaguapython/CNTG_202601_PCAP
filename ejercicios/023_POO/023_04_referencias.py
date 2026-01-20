class Director:
    def __init__(self, nombre, nacionalidad, anyo):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.anyo = anyo
    def saludar(self):
        print(f'Hola, soy {self.nombre}')

class Pelicula:
    def __init__(self, titulo : str, anyo : int, idioma : str, director : Director):
        self.titulo = titulo
        self.anyo = anyo
        self.idioma = idioma
        self.director = director

    def mostrar_informacion(self):
        print(self.titulo)
        print(self.anyo)
        print(self.idioma)
        self.director.saludar()

pedro = Director('Pedro Almodovar', 'Español', 1966)
tacones_lejanos = Pelicula('Tacones lejanos', 1988, 'Castellano', pedro)
tacones_lejanos.mostrar_informacion()


