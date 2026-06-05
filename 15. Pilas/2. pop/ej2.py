""" Tienes una pila de misiones pendientes. Tu equipo las completa de una en una empezando 
por la más urgente que está en el tope.
Lo que debes hacer paso a paso:
1. Crea una pila llamada misiones con estas 4 misiones ya cargadas:
   ["Buscar combustible",
    "Reparar generador",
    "Conseguir medicinas",
    "Rescatar a Luis"]
2. Imprime al inicio:
   "--- MISIONES PENDIENTES ---"
   "[estado de la pila]"
3. Vacía toda la pila con pop() dentro de un while
4. Dentro del while imprime por cada misión:
   "✅ Misión completada: [nombre de la misión]"
   "Misiones restantes: X"
5. Cuando no queden misiones imprime:
   "📋 Todas las misiones completadas, búnker seguro"
   
Lo que debe imprimir tu código:
--- MISIONES PENDIENTES ---
['Buscar combustible', 'Reparar generador', 'Conseguir medicinas', 'Rescatar a Luis']

✅ Misión completada: Rescatar a Luis
Misiones restantes: 3

✅ Misión completada: Conseguir medicinas
Misiones restantes: 2

✅ Misión completada: Reparar generador
Misiones restantes: 1

✅ Misión completada: Buscar combustible
Misiones restantes: 0

📋 Todas las misiones completadas, búnker seguro"""
Misiones=["Buscar combustible",
    "Reparar generador",
    "Conseguir medicinas",
    "Rescatar a Luis"]
print(f"Misiones pendientes: {Misiones}")
while Misiones:
    mision_completada=Misiones.pop()
    print(f"✅ Misión completada: {mision_completada}")
    print(f"Misiones restantes: {len(Misiones)}")
print("📋 Todas las misiones completadas, búnker seguro")