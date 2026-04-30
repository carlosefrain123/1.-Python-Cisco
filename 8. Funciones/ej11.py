""" Ejercicio 8 → Promedio de notas
Usando las funciones anteriores, calcula el promedio
de 3 notas y clasifica el resultado.
Si alguna nota es inválida devuelve None.

promedio_notas(15, 18, 12)  → "Bueno" (promedio: 15)
promedio_notas(8, 6, 10)    → "Desaprobado" (promedio: 8)
promedio_notas(25, 15, 12)  → None """



""" Solución mía:
    def promedio_notas(n1,n2,n3):
    if n1<0 or n1>20 or n2<0 or n2>20 or n3<0 or n3>20:
        return None
    return (n1+n2+n3)/3
print(promedio_notas(15, 18, 12))
print(promedio_notas(8, 6, 10))
print(promedio_notas(25, 15, 12)) """

def validar_nota(nota):
    if nota<0 or nota>20:
        return None
    return nota
def promedio_notas(n1,n2,n3):
    if validar_nota(n1) is None:
        return None
    elif validar_nota(n2) is None:
        return None
    elif validar_nota(n3) is None:
        return None
    return (n1+n2+n3)/3
print(promedio_notas(15, 18, 12))
print(promedio_notas(8, 6, 10))
print(promedio_notas(25, 15, 12))