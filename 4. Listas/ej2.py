hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
valor_a_reemplazar=int(input("Ingrese un valor: "))
hat_list[2]=valor_a_reemplazar
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[-1]
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print(hat_list)
print(len(hat_list))
