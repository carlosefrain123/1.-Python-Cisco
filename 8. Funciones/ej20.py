""" Caso 4: ¿Es nota aprobatoria?
Usando las funciones anteriores, verifica si una nota aprueba.
Aprueba si es mayor o igual a 11.
Si es inválida devuelve None.

# Prueba
test_data = [15, 8, 25, 0, 20]
expected  = [True, False, None, False, True]

es_aprobado(15) → True
es_aprobado(8)  → False
es_aprobado(25) → None


"""
def verificar_nota(nota):
    if nota<0 or nota>20:
        return None
    if nota<11:
        return False
    else:
        return True
test_data = [15, 8, 25, 0, 20]
expected  = [False, False, None, False, True]

for i in range(len(test_data)):
    valor_nota=verificar_nota(test_data[i])
    """ print(valor_nota) """
    if valor_nota==expected[i]:
        print("Ok")
    else:
        print("Error")