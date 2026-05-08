import math

# Raíz cuadrada
math.sqrt(25)        # → 5.0

# Potencia
math.pow(2, 3)       # → 8.0  (igual que 2**3 pero retorna float)

# Redondeo
math.floor(4.9)      # → 4  (hacia abajo)
math.ceil(4.1)       # → 5  (hacia arriba)

# Valor absoluto
math.fabs(-10)       # → 10.0

# Logaritmos
math.log(100)        # → valor de e**x
math.log(100, 10)    # → 2.0  (log base 10 de 100)
math.log2(8)         # → logaritmo binario de x (más preciso que log(x, 2))
math.log10(8)        # → logaritmo decimal de x (más preciso que log(x, 10))

# Constantes
math.pi              # → 3.141592653589793
math.e               # → 2.718281828459045

#trigonometria
math.sin(10)         # seno
math.cos(10)         # coseno
math.tan(10)         # tangente
math.asin(10)        # arcoseno
math.acos(10)        # arcocoseno
math.atan(10)        # arcotangente

#medidciones de angulos
math.radians(10)     # radianes
math.degrees(10)     # radianes en grados

#análogos hiperbólicos
math.sinh(10)        # seno hiperbólico
math.cosh(10)        # coseno hiperbólico
math.tanh(10)        # tangente hiperbólica
math.asinh(10)       # arcoseno hiperbólico
math.acosh(10)       # arcocoseno hiperbólico
math.atanh(10)       # arcotangente hiperbólico

#funciones de propósito general
math.trunc(10)       # el valor de x truncado a un entero (ten cuidado, no es equivalente a ceil o floor).
math.factorial(10)   # devuelve x! (x tiene que ser un valor entero y no negativo)
math.hypot(10,2)     # devuelve la longitud de la hipotenusa de un triángulo rectángulo con las longitudes de los catetos iguales a (x) y (y) (lo mismo que sqrt(pow(x, 2) + pow(y, 2)) pero más preciso).