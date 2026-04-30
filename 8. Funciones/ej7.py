""" Ejercicio 4 → Validar temperatura
Es válida si está entre -90°C y 60°C
(temperaturas reales en la Tierra).
Si no es válida devuelve None.

validar_temp(25)   → 25
validar_temp(-91)  → None
validar_temp(61)   → None """

def validar_temp(temp):
    if temp<-90 or temp>60:
        return None
    return temp
print(validar_temp(25))
print(validar_temp(-91))
print(validar_temp(61))