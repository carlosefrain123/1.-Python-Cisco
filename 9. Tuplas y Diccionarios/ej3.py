diccionario={}

while True:
    animales=input("Ingrese los animales: ")
    if animales=="":
        break
    edad=int(input("Ingrese la edad de los animales: "))
    if edad not in range(0,11):
        break
    print("nombre:", animales)
    print("edad:", edad)
    