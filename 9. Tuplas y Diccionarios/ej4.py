""" Guardar en el diccionario """
diccionario={}
while True:
    nombre=input("Ingrese nombre: ")
    if nombre=="":
        break
    edad=int(input("Ingrese edad: "))
    if edad not in range(0,21):
        break
    if nombre in diccionario:
        print("Nombre guardado")
        diccionario[nombre]+=edad
    else:
        print("Guardando...")
        diccionario[nombre]=edad
print(diccionario)
        