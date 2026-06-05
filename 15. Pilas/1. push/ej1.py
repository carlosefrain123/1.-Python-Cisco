""" Ejercicio 1 — Cargando la mochila
Estás preparando tu mochila antes de salir del búnker. Tu líder te pide registrar todo lo que cargas.
Lo que debes hacer paso a paso:
1. Crea una pila vacía llamada mochila
2. Agrega estos 4 objetos en este orden:
   - "Pistola"
   - "Botiquín"
   - "Linterna"
   - "Rifle"
3. Después de agregar cada objeto imprime:
   "Mochila: [estado actual de la pila]"
4. Al final imprime:
   "Total objetos: X"Lo que debe imprimir tu código:
Mochila: ['Pistola']
Mochila: ['Pistola', 'Botiquín']
Mochila: ['Pistola', 'Botiquín', 'Linterna']
Mochila: ['Pistola', 'Botiquín', 'Linterna', 'Rifle']
Total objetos: 4 """
mochila=[]
mochila.append("Pistola")
print(mochila)
mochila.append("Botiquín")
print(mochila)
mochila.append("Linterna")
print(mochila)
mochila.append("Rifle")
print(mochila)
print(f"Total de objetos: {len(mochila)}")