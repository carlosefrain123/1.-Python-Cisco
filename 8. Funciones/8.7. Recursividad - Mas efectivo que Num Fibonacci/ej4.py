""" Ejercicio 2 → Cuenta regresiva
cuenta(5) → 5, 4, 3, 2, 1, ¡Despegue! """
def cuenta(n):
    if n<=0:
        return print("¡Despegue!")
    print(n)
    return cuenta(n-1)
print(cuenta(5))