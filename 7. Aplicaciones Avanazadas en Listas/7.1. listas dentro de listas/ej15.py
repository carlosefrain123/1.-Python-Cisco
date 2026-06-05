""" Estás coordinando los equipos de defensa del búnker.
Cada lista contiene: [nombre_lider, *miembros, *armas]
donde los primeros datos son personas y los últimos son armas.

equipos = [
    ["Rick",     "Daryl", "Glenn",    "AK-47", "Pistola", "Ballesta"],
    ["Michonne", "Carol", "Maggie",   "Katana", "Escopeta", "Granada"],
    ["Negan",    "Dwight","Simon","Lucille", "AK-47", "Pistola", "Mina"]
]
personas = 3  # los primeros 3 elementos son personas
armas    = 3  # los últimos 3 elementos son armas (excepto equipo 3 que tiene 4)

Tu tarea es:
1. Imprimir líder, miembros y armas de cada equipo por separado
2. Contar el total de personas y armas en el búnker
3. Encontrar al equipo con más armas
4. Verificar si el arma "AK-47" está en más de un equipo
   y mostrar en cuáles """
   
equipos = [
    ["Rick",     "Daryl", "Glenn",    "AK-47", "Pistola", "Ballesta"],
    ["Michonne", "Carol", "Maggie",   "Katana", "Escopeta", "Granada"],
    ["Negan",    "Dwight","Simon","Lucille", "AK-47", "Pistola", "Mina"]
]
personas = 3  # los primeros 3 elementos son personas
armas    = 3  # los últimos 3 elementos son armas (excepto equipo 3 que tiene 4)
print("1. Imprimir líder, miembros y armas de cada equipo por separado")
