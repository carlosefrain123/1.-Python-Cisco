# I. Módulo random
# random() y seed()
import random

# random() → genera un float entre 0.0 y 1.0
print(random.random())      # → ej: 0.5714025946899135

# seed() → fija el punto de inicio, hace el random predecible
random.seed(42)
print(random.random())      # → siempre 0.6394267984578837
print(random.random())      # → siempre 0.025010755222666936

#seed() se usa para pruebas — cuando necesitas que el "aleatorio" sea siempre igual.

# II. randrange() y randint()
import random

# randrange(fin) → entre 0 y fin (sin incluir fin)
print(random.randrange(10))           # → 0 al 9

# randrange(inicio, fin) → entre inicio y fin (sin incluir fin)
print(random.randrange(5, 15))        # → 5 al 14

# randrange(inicio, fin, incremento) → solo números pares, de 5 en 5, etc
print(random.randrange(0, 20, 2))     # → 0,2,4,6...18  (solo pares)
print(random.randrange(0, 50, 5))     # → 0,5,10,15...45

# randint(izquierda, derecha) → entre ambos INCLUSIVE (incluye el fin)
print(random.randint(1, 10))          # → 1 al 10

# III. choice() y sample()
import random

lista = [10, 20, 30, 40, 50]

# shuffle() → Mexcla aleatoriamente los elementos de una secuencia mutable, como una lista, directamente en su lugar
print(random.shuffle(lista))         # → ej: [30, 10, 50, 20, 40]

# choice() → elige UN elemento aleatorio de la lista
print(random.choice(lista))           # → ej: 30

# sample() → elige VARIOS elementos sin repetir
print(random.sample(lista, 3))        # → ej: [20, 50, 10]
print(random.sample(lista, 2))        # → ej: [40, 30]

# También funciona con strings
letras = ["a", "b", "c", "d", "e"]
print(random.choice(letras))          # → ej: "c"
print(random.sample(letras, 3))       # → ej: ["e", "a", "c"]