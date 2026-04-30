""" Ejercicio 3 → Potencia
potencia(2, 4) = 2 × 2 × 2 × 2 = 16 """
def valor(base,potencia):
    if potencia==0:
        return 1
    
    return base*valor(base,potencia-1)
print(valor(2,4))