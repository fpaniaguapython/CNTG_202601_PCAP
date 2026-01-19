class Enemigo:
    def __init__(self, id, nombre, x, y, salud, velocidad, imagen):
        self.id = id
        self.nombre = nombre
        self.x = x
        self.y = y
        self.salud = salud
        self.velocidad = velocidad
        self.imagen = imagen
        self.vivo = True
    
    def mover(self, dx, dy):
        self.x+=dx
        self.y+=dy


sauron = Enemigo(id=1, nombre="Sauron", x=0, y=0, salud=100, velocidad=1, imagen="sauron.png")
sauron.mover(2,0)
sauron.mover(2,0)
