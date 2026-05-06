numeros = ["1", "2", "tres", "4"]
for i in numeros:
    try:
        convertir=int(i)
        print(convertir)
    except ValueError:
        print("Error")