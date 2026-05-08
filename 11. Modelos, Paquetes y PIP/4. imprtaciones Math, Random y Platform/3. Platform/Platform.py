# I. platform() — Info general del sistema
import platform

print(platform.platform())   
# → 'Windows-10-10.0.19041-SP0'
# → 'Linux-5.4.0-42-generic-x86_64'
# → 'macOS-12.0-x86_64'
# Imagínatelo así: le preguntas a tu computadora "¿quién eres?" y te da toda su presentación de golpe.

# II. processor() — El procesador
import platform

print(platform.processor())  
# → 'Intel64 Family 6 Model 142'
# → 'x86_64'
# → 'arm'
# Imagínatelo así: le preguntas "¿qué cerebro tienes?" — te dice qué procesador tiene la máquina.

# III. system() — El sistema operativo
import platform

print(platform.system())   
# → 'Windows'
# → 'Linux'
# → 'Darwin'  (así llama macOS)
# Imagínatelo así: le preguntas "¿en qué sistema corres?" — solo te dice el nombre limpio, sin detalles.

# IV. version() — La versión del sistema
import platform

print(platform.version())  
# → '10.0.19041'       (Windows)
# → '#47-Ubuntu SMP'   (Linux)
# Imagínatelo así: es el complemento de system() — si system() te dice "Windows", version() te dice "¿qué versión de Windows?"

# V. python_implementation() — Qué versión de Python corre
import platform

print(platform.python_implementation())  
# → 'CPython'    (la más común)
# → 'PyPy'
# → 'Jython'
# Imagínatelo así: Python tiene distintas "versiones del motor" — esta función te dice cuál motor está usando tu máquina. La mayoría usa CPython sin saberlo.

# VI. python_version_tuple() — La versión de Python en partes
import platform

print(platform.python_version_tuple())  
# → ('3', '10', '4')
# Te devuelve una tupla con 3 partes:
version = platform.python_version_tuple()
print(version[0])   # → '3'   (versión mayor)
print(version[1])   # → '10'  (versión menor)
print(version[2])   # → '4'   (parche)
# Imagínatelo así: en vez de darte "3.10.4" todo junto, te lo da separado en cajitas para que puedas usar cada parte por separado.

#Todo junto — ejemplo real
import platform

print(platform.system())                  # → Windows
print(platform.version())                 # → 10.0.19041
print(platform.processor())              # → Intel64...
print(platform.python_implementation())  # → CPython
print(platform.python_version_tuple())   # → ('3', '10', '4')