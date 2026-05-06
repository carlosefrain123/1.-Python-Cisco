""" Ejercicio 2 → Input inválido """
try:
    valor=input("Ingrese un valor: ")
    resultado=int(valor)
    print(resultado)
except ValueError:
    print("Error..")