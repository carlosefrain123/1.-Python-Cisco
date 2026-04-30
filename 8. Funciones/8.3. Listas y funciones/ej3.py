def message(cv):
    lista=[]
    for i in range(cv):
        valores=int(input("Ingrese los valores: "))
        lista.append(valores)
    print(lista)
    return cv
cv=int(input("Ingrese la cantidad de valores: "))
message(cv)
""" lista=[]
    cv=int(input("Ingrese la cantidad de valores: "))
    for i in range(cv):
        valores=int(input("Ingrese los valores: "))
        lista.append(valores)
    print(lista) """