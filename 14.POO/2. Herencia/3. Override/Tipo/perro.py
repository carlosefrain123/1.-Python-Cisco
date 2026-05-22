from Tipo.animal import Animal
class Perro(Animal):
    def hablar(self):              # sobreescribe el del padre
        print("¡Guau!")