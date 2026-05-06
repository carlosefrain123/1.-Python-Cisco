""" Ejercicio 2 → Input inválido """
try:
    valor=int(input("Ingrese el valor correspondiente: "))
    print(valor)
except ValueError:
    print("El valor tiene que ser un número.")