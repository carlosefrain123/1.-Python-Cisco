def suma(a,b):
    try:
        respuesta=a+b
        return respuesta
    except TypeError:
        return "Error"
print(suma(10,50))
print(suma(10,"a"))
