from Tipo.animal import Animal
class Gato(Animal):
    def hablar(self):              # sobreescribe el del padre
        print("¡Miau!")