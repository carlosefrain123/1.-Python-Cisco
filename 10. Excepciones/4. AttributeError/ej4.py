""" Ejercicio 3 → Atributo inexistente """
try:
    texto = "hola"
    print(texto.longitud)
except AttributeError:
    print("Error: los textos no tienen el atributo longitud")
