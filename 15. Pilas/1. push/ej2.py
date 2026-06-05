""" Tu equipo va rescatando sobrevivientes y los registra en una pila.
Lo que debes hacer paso a paso:
1. Crea una pila vacía llamada rescatados
2. Agrega estos 3 sobrevivientes en este orden:
   - "Efrain - sano"
   - "Ana - herida leve"
   - "Carlos - sano"
3. Después de agregar cada sobreviviente imprime:
   "Rescatados hasta ahora: [estado actual de la pila]"
4. Al final imprime:
   "Total rescatados: X"
   "Último en entrar: [nombre del último]"
Lo que debe imprimir tu código:
Rescatados hasta ahora: ['Efrain - sano']
Rescatados hasta ahora: ['Efrain - sano', 'Ana - herida leve']
Rescatados hasta ahora: ['Efrain - sano', 'Ana - herida leve', 'Carlos - sano']
Total rescatados: 3
Último en entrar: Carlos - sano """
rescatados=[]
rescatados.append("Efrain - sano")
print(rescatados)
rescatados.append("Ana - herida leve")
print(rescatados)
rescatados.append("Carlos - sano")
print(rescatados)
print(f"Total Rescatados: {len(rescatados)}")
print(f"Último a entrar: {rescatados[-1]}")