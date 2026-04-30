""" Ejercicio 5 → Clasificar temperatura
Usando la función anterior, clasifica la temperatura:
-90 a 0   → "Muy frío"
1 a 15    → "Frío"
16 a 25   → "Templado"
26 a 60   → "Caluroso"
None      → "Temperatura inválida"

clasificar_temp(−5)  → "Muy frío"
clasificar_temp(10)  → "Frío"
clasificar_temp(20)  → "Templado"
clasificar_temp(35)  → "Caluroso"
clasificar_temp(100) → "Temperatura inválida" """
def validar_temp(temp):
    if temp<-90 or temp>60:
        return None
    return temp
def clasificar_temp(ct):
    if validar_temp(ct) is None:
        return "Temperatura inválida"
    if ct<=0:
        return "Muy Frio"
    elif ct<=15:
        return "Frío"
    elif ct<=25:
        return "Templado"
    else:
        return "Caluroso"
    
print(clasificar_temp(-5))
print(clasificar_temp(10))
print(clasificar_temp(20))
print(clasificar_temp(35))
print(clasificar_temp(100))


