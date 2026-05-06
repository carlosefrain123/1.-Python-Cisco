""" Ejercicio 3 → Convertir lista de textos """
numeros = ["1", "2", "tres", "4"]
for i in numeros:
    try:
        convertir_numero=int(i)
        print(convertir_numero)
    except:
        print("El ",i," no se puede convertir en número")