class Animal:
    pass

class Mamifero(Animal):
    pass

class Vaca(Mamifero):
    pass

class Lagarto(Animal):
    pass

marela = Vaca()
# isinstance --> Indica si un OBJETO es instancia de una CLASE
print('1',isinstance(marela, Vaca)) # True
print('2',isinstance(marela, Mamifero)) # True
print('3',isinstance(marela, Animal)) # True
print('4',isinstance(marela, object)) # True
print('5',isinstance(marela, Lagarto)) # False
print('6',isinstance(marela, list)) # False
print('7',isinstance(marela, (Mamifero, list, str))) # True

# issubclass
print('8',issubclass(Mamifero, Animal)) # True
print('9',issubclass(Vaca, Mamifero)) # True
print('10',issubclass(Vaca, Animal)) # True
print('11',issubclass(Lagarto, Animal)) # True
print('12',issubclass(Lagarto, Vaca)) # False