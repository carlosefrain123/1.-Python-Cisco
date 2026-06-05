""" Ejercicio 1 — Revisando antes de salir
Antes de salir del búnker revisas qué arma tienes en el tope de 
tu mochila para decidir si es seguro salir.
Lo que debes hacer paso a paso:
1. Crea una pila llamada mochila con estas 3 armas ya cargadas:
   ["Cuchillo", "Pistola", "Rifle"]
2. Imprime al inicio:
   "--- REVISIÓN DE MOCHILA ---"
3. Usa peek ([-1]) para ver el arma del tope sin sacarla
4. Imprime:
   "Arma en el tope: [arma]"
5. Evalúa con if/elif/else:
   - Si es "Rifle"    → "✅ Tienes Rifle, salida segura"
   - Si es "Pistola"  → "⚠️ Tienes Pistola, sal con cuidado"
   - Si es otra cosa  → "❌ Arma débil, no salgas"
6. Al final imprime la pila completa para verificar que no cambió:
   "Mochila sin cambios: [estado de la pila]"
Lo que debe imprimir tu código:
--- REVISIÓN DE MOCHILA ---
Arma en el tope: Rifle
✅ Tienes Rifle, salida segura
Mochila sin cambios: ['Cuchillo', 'Pistola', 'Rifle'] """
Mochila=["Cuchillo", "Pistola", "Rifle"]
print("--- REVISIÓN DE MOCHILA ---")
herramienta=Mochila[-1]
if herramienta=="Rifle":
    print("✅ Tienes Rifle, salida segura")
elif herramienta=="Pistola":
    print("⚠️ Tienes Pistola, sal con cuidado")
else:
    print("❌ Arma débil, no salgas")
print(f"Mochila sin cambios: {Mochila}")