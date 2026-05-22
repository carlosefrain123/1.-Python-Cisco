from Tipos.animal import Animal
class Perro(Animal):
    def __init__(self, nombre,raza):
        super().__init__(nombre)
        self.raza=raza
    def info(self):
        print(f"Soy {self.nombre} y soy de raza {self.raza}")