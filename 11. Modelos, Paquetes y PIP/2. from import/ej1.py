# Forma normal - importas todo, usas el prefijo
import math
print(math.sin(math.pi))

# Forma selectiva - importas solo lo que necesitas, sin prefijo
from math import sin, pi
print(sin(pi))        # → -2.4492935982947064e-17 (básicamente 0)