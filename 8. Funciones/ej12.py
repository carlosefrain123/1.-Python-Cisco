""" Ejercicio 9 → Validar hora
Es válida si hora está entre 0 y 23
y minutos entre 0 y 59.
Si no es válida devuelve None.

validar_hora(12, 30)  → "12:30"
validar_hora(25, 30)  → None
validar_hora(12, 61)  → None """

def hora_min(h,m):
    if h<0 or h>24 or m<0 or m>60:
        return None
    return f"{h}:{m:02d}"
print(hora_min(12, 30))
print(hora_min(25, 30))
print(hora_min(12, 61))
