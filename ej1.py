""" #Proyecto Cisco:
Escenario
Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, 
hemos decidido simplificar el juego. Aquí están nuestras reglas:

la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, por ejemplo un valor 
entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado; el programa verifica si el juego ha terminado -
existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana;
la maquina responde con su movimiento y se verifica el estado del juego; no se debe implementar algún tipo de inteligencia artificial 
- la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.
El ejemplo del programa es el siguiente:
    
Requerimientos
Implementa las siguientes características:

el tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra lista de tres elementos 
(la lista interna representa las filas) de manera que todos los cuadros puedas ser accedidos empleado la siguiente sintaxis:

board[row][column]
 

cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito representando el número del cuadro 
(dicho cuadro se considera como libre)
la apariencia de tablero debe de ser igual a la presentada en el ejemplo.
implementa las funciones definidas para ti en el editor.

Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada randrange(). 
El siguiente ejemplo muestra como utilizarla (El programa imprime 10 números aleatorios del 1 al 8).

Nota: la instrucción from-import provee acceso a la función randrange definida en un módulo externo de Python denominado random.

from random import randrange
 
for i in range(10):
    print(randrange(8))
 """
from random import randrange

def mostrar_tablero(tablero):
    print("+-------+-------+-------+")
    for fila in tablero:
        print("|       |       |       |")
        print("|", "   |   ".join(fila), "|")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def casillas_libres(tablero):
    libres = []
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] not in ['X', 'O']:
                libres.append((fila, columna))
    return libres

def hay_ganador(tablero, simbolo):
    # filas
    for fila in range(3):
        if tablero[fila][0] == simbolo and \
           tablero[fila][1] == simbolo and \
           tablero[fila][2] == simbolo:
            return True
    # columnas
    for columna in range(3):
        if tablero[0][columna] == simbolo and \
           tablero[1][columna] == simbolo and \
           tablero[2][columna] == simbolo:
            return True
    # diagonal izquierda
    if tablero[0][0] == simbolo and \
       tablero[1][1] == simbolo and \
       tablero[2][2] == simbolo:
        return True
    # diagonal derecha
    if tablero[0][2] == simbolo and \
       tablero[1][1] == simbolo and \
       tablero[2][0] == simbolo:
        return True
    return False

def turno_jugador(tablero):
    while True:
        casilla = int(input("Ingresa tu movimiento: "))
        if casilla < 1 or casilla > 9:
            print("Número inválido, intenta de nuevo")
            continue
        fila = (casilla - 1) // 3
        columna = (casilla - 1) % 3
        if tablero[fila][columna] in ['X', 'O']:
            print("Casilla ocupada, intenta de nuevo")
            continue
        tablero[fila][columna] = 'O'
        break

def turno_maquina(tablero):
    libres = casillas_libres(tablero)
    if libres:
        indice = randrange(len(libres))
        fila, columna = libres[indice]
        tablero[fila][columna] = 'X'

# ─── JUEGO ───
tablero = [
    ['1', '2', '3'],
    ['4', 'X', '6'],
    ['7', '8', '9']
]

mostrar_tablero(tablero)

while True:
    # turno del jugador
    turno_jugador(tablero)
    mostrar_tablero(tablero)

    if hay_ganador(tablero, 'O'):
        print("¡Has Ganado!")
        break

    libres = casillas_libres(tablero)
    if not libres:
        print("¡Empate!")
        break

    # turno de la máquina
    turno_maquina(tablero)
    mostrar_tablero(tablero)

    if hay_ganador(tablero, 'X'):
        print("¡La máquina ha ganado!")
        break

    libres = casillas_libres(tablero)
    if not libres:
        print("¡Empate!")
        break