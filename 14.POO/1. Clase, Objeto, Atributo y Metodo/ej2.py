class Auto:
    def __init__(self, marca, año):
        self.marca     = marca   # atributo
        self.año       = año     # atributo
        self.encendido = False  # atributo (estado)

    def encender(self):        # método
        self.encendido = True
        print(f"El {self.marca} está encendido 🔑")

    def apagar(self):          # método
        self.encendido = False
        print(f"El {self.marca} está apagado")
        
auto1 = Auto("Toyota", 2022)
auto2 = Auto("Ford",   2020)

auto1.encender()
auto2.apagar()
print(auto1.encendido)   # → True