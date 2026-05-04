""" Usando todas las funciones anteriores, genera un
reporte completo del estudiante con 3 notas.
Si alguna nota es inválida devuelve None.

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

reporte(15, 8, 12) →
    Nota 1: 15 → Bueno ✅
    Nota 2: 8  → Desaprobado ❌ (le faltan 3 puntos)
    Nota 3: 12 → Regular ✅
    Promedio: Regular """
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
    elif nota<=16:
        return "Bueno"
    else:
        return "Excelente"
def nota_restantes(nota):
    if clasificar_nota(nota)!="Desaprobado":
        return 0
    else:
        puntos_faltantes=11-nota
        return puntos_faltantes
""" print(nota_restantes(9)) """
def promedio(n1,n2,n3):
    if validar_nota(n1) is None:
        return None
    if validar_nota(n2) is None:
        return None
    if validar_nota(n3) is None:
        return None
    promedio=(n1+n2+n3)/3
    
    return "El promedio es ",promedio,"->",clasificar_nota(promedio),"->",nota_restantes(promedio)
print(promedio(8,6,7))