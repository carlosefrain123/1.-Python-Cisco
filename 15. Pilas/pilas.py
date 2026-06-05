""" Una pila es como una pila de platos:
        [Plato 3]  ← último en entrar, primero en salir
        [Plato 2]
        [Plato 1]  ← primero en entrar, último en salir
La regla de oro de una pila:

El último que entra es el primero que sale

En el mundo zombie imagínatelo así:
        [Rifle]     ← lo usas primero
        [Escopeta]
        [Pistola]   ← lo usas último

push() — Agregar al tope
Imagínatelo así: apilas un plato encima de los demás.
Ejemplo básico
pythonpila = []             # pila vacía

pila.append("A")      # push
pila.append("B")      # push
pila.append("C")      # push

print(pila)           # → ['A', 'B', 'C']
#                              ↑           ↑
#                         primero       tope
Ejemplo zombie
pythonmochila = []

mochila.append("Pistola")    # push → entra primero
mochila.append("Botiquín")   # push → entra segundo
mochila.append("Rifle")      # push → entra al tope

print(mochila)
# → ['Pistola', 'Botiquín', 'Rifle']
#                              ↑
#                           tope (lo primero que usarías)
Otro ejemplo zombie
pythonmisiones = []

misiones.append("Buscar agua")         # push
misiones.append("Reparar generador")   # push
misiones.append("Rescatar a Luis")     # push → más urgente

print(misiones)
# → ['Buscar agua', 'Reparar generador', 'Rescatar a Luis']
print(f"Misiones pendientes: {len(misiones)}")
# → Misiones pendientes: 3

pop() — Sacar del tope
Imagínatelo así: quitas el plato de arriba — ese plato desaparece de la pila.
Ejemplo básico
pythonpila = ["A", "B", "C"]

sacado = pila.pop()    # saca "C" del tope
print(sacado)          # → C
print(pila)            # → ['A', 'B']
#                                   ↑
#                               ahora "B" es el tope
Ejemplo zombie
pythonmochila = ["Pistola", "Botiquín", "Rifle"]

usado = mochila.pop()        # saca el Rifle
print(f"Usaste: {usado}")    # → Usaste: Rifle
print(mochila)               # → ['Pistola', 'Botiquín']

usado = mochila.pop()        # saca el Botiquín
print(f"Usaste: {usado}")    # → Usaste: Botiquín
print(mochila)               # → ['Pistola']
Otro ejemplo zombie — vaciando misiones
pythonmisiones = ["Buscar agua", "Reparar generador", "Rescatar a Luis"]

while misiones:                          # mientras haya misiones
    completada = misiones.pop()
    print(f"✅ Completada: {completada}")

print("📋 Sin misiones pendientes")
# → ✅ Completada: Rescatar a Luis
# → ✅ Completada: Reparar generador
# → ✅ Completada: Buscar agua
# → 📋 Sin misiones pendientes

peek() — Ver el tope sin sacar
Imagínatelo así: miras el plato de arriba pero no lo tocas — la pila queda igual.
Ejemplo básico
pythonpila = ["A", "B", "C"]

tope = pila[-1]        # peek → solo miras
print(tope)            # → C
print(pila)            # → ['A', 'B', 'C']  ← no cambió nada
Ejemplo zombie
pythonmochila = ["Pistola", "Botiquín", "Rifle"]

proximo = mochila[-1]                    # peek
print(f"Próximo a usar: {proximo}")      # → Próximo a usar: Rifle
print(f"Mochila: {mochila}")             # → Mochila: ['Pistola', 'Botiquín', 'Rifle']
#                                          la mochila NO cambió ✅
Otro ejemplo zombie — decidiendo si atacar
pythonarmas = ["Cuchillo", "Escopeta", "Pistola"]

arma_disponible = armas[-1]              # peek

if arma_disponible == "Pistola":
    print("✅ Tienes pistola, puedes atacar")
elif arma_disponible == "Escopeta":
    print("💪 Tienes escopeta, ataque fuerte")
else:
    print("⚠️ Solo tienes cuchillo, evita el combate")

print(f"Armas: {armas}")                 # la pila no cambió ✅
# → ✅ Tienes pistola, puedes atacar
# → Armas: ['Cuchillo', 'Escopeta', 'Pistola']

La diferencia entre los 3
pythonpila = ["Pistola", "Botiquín", "Rifle"]

# push → agrega al tope
pila.append("Granada")
print(pila)   # → ['Pistola', 'Botiquín', 'Rifle', 'Granada']

# peek → solo mira el tope, NO modifica
tope = pila[-1]
print(tope)   # → Granada
print(pila)   # → ['Pistola', 'Botiquín', 'Rifle', 'Granada'] ← igual

# pop → saca del tope, SÍ modifica
sacado = pila.pop()
print(sacado) # → Granada
print(pila)   # → ['Pistola', 'Botiquín', 'Rifle']
¿Qué hace?¿Modifica la pila?append() pushAgrega al tope✅ Sí[-1] peekSolo mira el tope❌ Nopop()Saca del tope✅ Sí

Todo junto — Ejemplo zombie completo
python# Simulas un día en el búnker

inventario = []

# Mañana — cargas tu mochila (push)
print("--- MAÑANA ---")
inventario.append("Pistola")
inventario.append("Botiquín")
inventario.append("Rifle")
print(f"Mochila: {inventario}")
# → Mochila: ['Pistola', 'Botiquín', 'Rifle']

# Antes de salir — revisas qué tienes (peek)
print("\n--- ANTES DE SALIR ---")
proximo = inventario[-1]
print(f"Tienes en el tope: {proximo}")
# → Tienes en el tope: Rifle

# En combate — usas items (pop)
print("\n--- EN COMBATE ---")
usado = inventario.pop()
print(f"Usaste: {usado}")
# → Usaste: Rifle

usado = inventario.pop()
print(f"Usaste: {usado}")
# → Usaste: Botiquín

# Al volver — agregas lo que encontraste (push)
print("\n--- AL VOLVER ---")
inventario.append("Escopeta")
inventario.append("Vendas")
print(f"Mochila final: {inventario}")
# → Mochila final: ['Pistola', 'Escopeta', 'Vendas']

# Revisión final (peek)
print("\n--- REVISIÓN FINAL ---")
print(f"Próximo a usar: {inventario[-1]}")
# → Próximo a usar: Vendas

Resumen visual
inventario = []

append("Pistola")  →  ['Pistola']
append("Botiquín") →  ['Pistola', 'Botiquín']
append("Rifle")    →  ['Pistola', 'Botiquín', 'Rifle']
[-1]               →  'Rifle'  (pila no cambia)
pop()              →  ['Pistola', 'Botiquín']
pop()              →  ['Pistola']
append("Escopeta") →  ['Pistola', 'Escopeta'] """