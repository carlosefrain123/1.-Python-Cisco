""" Ejercicio 1 → Suma de números del 1 hasta n
suma(5) = 5 + 4 + 3 + 2 + 1 = 15 """
def sum(n):
    if n<=0:
        return 0
    return n+sum(n-1)
for n in range(1,6):
    print(n,"->",sum(n))