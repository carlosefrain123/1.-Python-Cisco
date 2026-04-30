def message(cn):
    lista=[]
    for i in range(cn):
        lista.append(i)
    print("La lista es: ",lista)
    return cn
cn=int(input("Ingrese los valores a ingresar: "))
message(cn)