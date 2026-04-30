"""
Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y 
devuelve el número de días del mes/año dado (mientras que solo febrero es sensible al 
valor year, tu función debería ser universal).

Recuerda:
si el número del año no es divisible entre cuatro, es un año común.
de lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
de lo contrario, si el número del año no es divisible entre 400, es un año común.
de lo contrario, es un año bisiesto.

La parte inicial de la función está lista. Ahora, haz que la función devuelva None 
si los argumentos no tienen sentido.

Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada 
(LAB 4.3.1.6). Puede ser muy útil. Te recomendamos que utilices una lista con los meses.
Puedes crearla dentro de la función - este truco acortará significativamente el código.

Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.

Ejemplo:

print(año_mes(2000, 2))   # 29 (bisiesto)
print(año_mes(1900, 2))   # 28 (no bisiesto)
print(año_mes(2023, 1))   # 31
print(año_mes(2023, 13))  # None
"""

def año_bisiesto(año):
    if año%4!=0:
        return False
    elif año%100:
        return True
    elif año%400:
        return False
    else:
        return True
def año_mes(año,mes):
    if mes<1 or mes>12:
        return None
    dia=[31,28,31,30,31,30,31,31,30,31,30,31]
    if mes==2 and año_bisiesto(año):
        return 29
    return dia[mes-1]
print(año_mes(2000, 2))
print(año_mes(1900, 2))
print(año_mes(2023, 1))