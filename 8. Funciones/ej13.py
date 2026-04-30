""" Ejercicio 10 → Minutos del día
Usando la función anterior, calcula cuántos
minutos han pasado desde las 00:00.
Si la hora es inválida devuelve None.

minutos_dia(0, 0)   → 0
minutos_dia(1, 30)  → 90
minutos_dia(12, 30) → 750
minutos_dia(25, 30) → None """

def validar_hora(h,m):
    if h<0 or h>24 or m<0 or m>60:
        return None
    return f"{h}:{m:02d}"
def minutos_dia(h,m):
    if validar_hora(h,m) is None:
        return None
    return (h*60)+m
print(minutos_dia(0, 0))
print(minutos_dia(1, 30))
print(minutos_dia(12, 30))
print(minutos_dia(25, 30))