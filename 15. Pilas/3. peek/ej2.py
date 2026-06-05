""" Tu líder quiere conocer la misión más urgente antes de asignar soldados. Solo quiere verla, no completarla todavía.
Lo que debes hacer paso a paso:
1. Crea una pila llamada misiones con estas 3 misiones ya cargadas:
   ["Buscar agua", "Reparar radio", "ZOMBIES EN LA PUERTA"]
2. Imprime al inicio:
   "--- CENTRO DE OPERACIONES ---"
3. Usa peek ([-1]) para ver la misión más urgente sin sacarla
4. Imprime:
   "🚨 Misión más urgente: [misión]"
5. Evalúa con if:
   - Si contiene "ZOMBIES" → imprime "💀 ¡PELIGRO MÁXIMO! Enviar todos los soldados"
   - Si no               → imprime "👍 Situación controlada, misión normal"
6. Al final imprime la pila completa para verificar que no cambió:
   "Misiones sin cambios: [estado de la pila]"
   "Total misiones pendientes: X"
Lo que debe imprimir tu código:
--- CENTRO DE OPERACIONES ---
🚨 Misión más urgente: ZOMBIES EN LA PUERTA
💀 ¡PELIGRO MÁXIMO! Enviar todos los soldados
Misiones sin cambios: ['Buscar agua', 'Reparar radio', 'ZOMBIES EN LA PUERTA']
Total misiones pendientes: 3 """
misiones=["Buscar agua", "Reparar radio", "ZOMBIES EN LA PUERTA"]
print("--- CENTRO DE OPERACIONES ---")
print(misiones)
print(f"🚨 Misión más urgente: {misiones[-1]}")
mision_ultima=misiones[-1]
if "Zombies" in misiones:
    print("💀 ¡PELIGRO MÁXIMO! Enviar todos los soldados")
else:
    print("👍 Situación controlada, misión normal")
print(f"Misiones sin cambios: {misiones}")
print(f"Total misiones pendientes: {len(misiones)}")
