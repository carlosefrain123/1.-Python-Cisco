""" Usando las funciones anteriores, calcula cuántos
puntos le faltan a una nota para aprobar.
Si ya aprobó devuelve 0.
Si es inválida devuelve None.

Recuerda 1:
Validar nota
Es válida si está entre 0 y 20.
Si no es válida devuelve None

Recuerda 2: Clasificar nota
0-10  → "Desaprobado"
11-13 → "Regular"
14-16 → "Bueno"
17-20 → "Excelente"
None  → "Nota inválida"

puntos_faltantes(15) → 0
puntos_faltantes(8)  → 3
puntos_faltantes(25) → None """

def validar_nota(nota):
    if nota<0 or nota>20:
        return None
    return nota
def clasificar_nota(nota):
    if validar_nota(nota) is None:
        return "Nota inválida"
    if nota<=10:
        return "Desaprobado"
    elif nota<=13:
        return "Regular"
    else:
        return "Excelente"
""" print(clasificar_nota(-1)) """
def puntos_faltantes(nota):
    if validar_nota(nota) is None:
        return None
    if clasificar_nota(nota)!="Desaprobado":
        return 0
    else:
        nota_faltante=11-nota
        return nota_faltante
print(puntos_faltantes(5))
print(puntos_faltantes(15))
print(puntos_faltantes(25))
