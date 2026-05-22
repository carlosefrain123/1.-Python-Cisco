class Perro:
    # __init__ es el constructor (se ejecuta al crear el objeto)
    def __init__(self, nombre, raza):
        self.nombre = nombre  # atributo
        self.raza   = raza    # atributo

    def ladrar(self):        # método
        print(f"¡Guau! Soy {self.nombre}!")

    def presentarse(self):  # método
        print(f"Soy {self.nombre}, un {self.raza}")

mi_perro    = Perro("Toby", "Labrador")   # objeto 1
otro_perro  = Perro("Luna", "Poodle")    # objeto 2

mi_perro.ladrar()          # llama al método
otro_perro.presentarse()   # llama al método

print(mi_perro.nombre)     # accede al atributo → Toby