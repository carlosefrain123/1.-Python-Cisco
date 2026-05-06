""" Ejercicio 6 → Validar edad """
def validad_edad(edad):
    try:
        edad_valida=int(edad)
        if edad_valida<0 or edad_valida>20:
            raise ValueError
        return edad_valida
    except ValueError:
        return "Error"
print(validad_edad(10))
print(validad_edad("Hola"))
