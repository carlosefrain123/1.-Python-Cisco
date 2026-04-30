""" Tu tarea es escribir y probar una función que toma tres argumentos 
(un año, un mes y un día del mes) y devuelve el día correspondiente del año, 
o devuelve None si cualquiera de los argumentos no es válido.
Debes utilizar las funciones previamente escritas y probadas. 
Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo. 
Recuerda:
si el número del año no es divisible entre cuatro, es un año común.
de lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
de lo contrario, si el número del año no es divisible entre 400, es un año común.
de lo contrario, es un año bisiesto.
Ejemplo:
print(año_mes_dia(2000, 12, 31))  # 366
print(año_mes_dia(2023, 1,  1))   # 1
print(año_mes_dia(2023, 3,  1))   # 60
print(año_mes_dia(2023, 13, 1))   # None
"""
def año_bisiesto(año):
    if año%4!=0:
        return False
    elif año%100!=0:
        return True
    elif año%400!=0:
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

def año_mes_dia(año,mes,dia):
    if mes<1 or mes>12:
        return None
    if dia<0 or dia>año_mes(año,mes):
        return None
    total=0
    for m in range(1,mes):
        total+=año_mes(año,m)
    total+=dia
    return total
print(año_mes_dia(2000, 12, 31))  # 366
print(año_mes_dia(2023, 1,  1))   # 1
print(año_mes_dia(2023, 3,  1))   # 60
print(año_mes_dia(2023, 13, 1))   # None