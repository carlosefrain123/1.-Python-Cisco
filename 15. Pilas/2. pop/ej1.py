""" Ejercicio 1 — Usando recursos en combate
Tienes una pila de recursos listos para usar en combate. Los usas de uno en uno empezando por el tope.
Lo que debes hacer paso a paso:
1. Crea una pila llamada recursos con estos 4 items ya cargados:
   ["Agua", "Vendas", "Botiquín", "Adrenalina"]
2. Saca 3 recursos con pop() uno por uno
3. Después de cada pop() imprime:
   "Usaste: [item sacado]"
   "Quedan: [estado actual de la pila]"
4. Al final imprime:
   "Recurso que sobró: [lo que quedó]"
Lo que debe imprimir tu código:
Usaste: Adrenalina
Quedan: ['Agua', 'Vendas', 'Botiquín']

Usaste: Botiquín
Quedan: ['Agua', 'Vendas']

Usaste: Vendas
Quedan: ['Agua']

Recurso que sobró: Agua """
recursos=["Agua", "Vendas", "Botiquín", "Adrenalina"]
print(recursos)
usado=recursos.pop()
print(f"Usaste: {usado}")
print(f"Quedan: {recursos}")
usado=recursos.pop()
print(f"Usaste: {usado}")
print(f"Quedan: {recursos}")
usado=recursos.pop()
print(f"Usaste: {usado}")
print(f"Quedan: {recursos}")
print(f"\nRecurso que sobró: {recursos[0]}")
