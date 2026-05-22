class Animal:
    def __init__(self,nombre):
        self.nombre=nombre
    def respirar(self):
        print(f"{self.nombre} está respirando")
    def comer(self):
        print(f"{self.nombre} está comiendo")