""" Ejercicio 6 → División en función """
def divsion(a,b):
    try:
        resultado=a/b
        return resultado
    except ZeroDivisionError:
        return "Error"
print(divsion(10,2))
print(divsion(10,0))
